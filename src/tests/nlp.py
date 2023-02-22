from transformers import AutoModelForMaskedLM
from transformers import AutoTokenizer
from datasets import load_dataset

import torch

model_checkpoint = "bert-base-uncased"
model = AutoModelForMaskedLM.from_pretrained(model_checkpoint)

distilbert_num_parameters = model.num_parameters() / 1_000_000
print(f"DistilBERT number of parameters: {round(distilbert_num_parameters)}M")

text = "the best video game is [MASK]."
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

inputs = tokenizer(text, return_tensors="pt")
token_logits = model(**inputs).logits
# Find the location of [MASK] and extract its logits
mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]
mask_token_logits = token_logits[0, mask_token_index, :]
# Pick the [MASK] candidates with the highest logits
top_5_tokens = torch.topk(mask_token_logits, 5, dim=1).indices[0].tolist()

for token in top_5_tokens:
    print(f"{text.replace(tokenizer.mask_token, tokenizer.decode([token]))}")

lyrics_dataset_obj = load_dataset("csv", data_files="data/dataset.csv")
lyrics_dataset = lyrics_dataset_obj["train"].train_test_split(test_size=0.2)
print(lyrics_dataset)

sample = lyrics_dataset["train"].shuffle(seed=42).select(range(3))

for row in sample:
    print(f"\n'>>> lyrics: {row['lyrics']}'")


def tokenize_function(examples):
    result = tokenizer(examples["lyrics"])
    if tokenizer.is_fast:
        result["word_ids"] = [result.word_ids(i) for i in range(len(result["input_ids"]))]
    return result

# Use batched=True to activate fast multithreading!
tokenized_datasets = lyrics_dataset.map(
    tokenize_function, batched=True, remove_columns=["id", "lang", "lyrics"]
)
print(tokenized_datasets)

chunk_size = 128
tokenized_samples = tokenized_datasets["train"][:3]

for idx, sample in enumerate(tokenized_samples["input_ids"]):
    print(f"'>>> Review {idx} length: {len(sample)}'")

concatenated_examples = {
    k: sum(tokenized_samples[k], []) for k in tokenized_samples.keys()
}
total_length = len(concatenated_examples["input_ids"])
print(f"'>>> Concatenated reviews length: {total_length}'")

chunks = {
    k: [t[i : i + chunk_size] for i in range(0, total_length, chunk_size)]
    for k, t in concatenated_examples.items()
}

for chunk in chunks["input_ids"]:
    print(f"'>>> Chunk length: {len(chunk)}'")

def group_texts(examples):
    # Concatenate all texts
    concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    # Compute length of concatenated texts
    total_length = len(concatenated_examples[list(examples.keys())[0]])
    # We drop the last chunk if it's smaller than chunk_size
    total_length = (total_length // chunk_size) * chunk_size
    # Split by chunks of max_len
    result = {
        k: [t[i : i + chunk_size] for i in range(0, total_length, chunk_size)]
        for k, t in concatenated_examples.items()
    }
    # Create a new labels column
    result["labels"] = result["input_ids"].copy()
    return result

lm_datasets = tokenized_datasets.map(group_texts, batched=True)
print(lm_datasets)