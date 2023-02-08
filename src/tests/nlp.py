from transformers import AutoModelForMaskedLM
from transformers import AutoTokenizer

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