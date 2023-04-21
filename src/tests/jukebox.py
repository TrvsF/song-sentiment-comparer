from transformers import AutoTokenizer, AutoModel, DataCollatorWithPadding, AutoModelForSequenceClassification
from datasets import load_dataset

jukebox_tokenizer = AutoTokenizer.from_pretrained("openai/jukebox-1b-lyrics")
jukebox_model     = AutoModel.from_pretrained("openai/jukebox-1b-lyrics")

sentiment_dataset_obj = load_dataset("csv", data_files="data/sentiment.csv")
sentiment_model       = sentiment_dataset_obj["train"].train_test_split(test_size=0.2)

sentiment_train = sentiment_model["train"].shuffle(seed=42)
sentiment_test  = sentiment_model["test"].shuffle(seed=42)

def preprocess_func(examples):
    return jukebox_tokenizer(examples["lyrics"], None)

tokenized_train = sentiment_train.map(preprocess_func, batched=True)
tokenized_test  = sentiment_test.map(preprocess_func, batched=True)

data_collector = DataCollatorWithPadding(tokenizer=jukebox_tokenizer)

model = AutoModelForSequenceClassification.from_pretrained("openai/jukebox-1b-lyrics", num_labels=2)