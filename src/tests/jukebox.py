from transformers import AutoTokenizer, TrainingArguments, Trainer, DataCollatorWithPadding, AutoModelForSequenceClassification
from datasets import load_dataset, load_metric
# from pandas import DataFrame

import numpy as np

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

sentiment_dataset_obj = load_dataset("csv", data_files="data/sentiment.csv")
sentiment_model       = sentiment_dataset_obj["train"].train_test_split(test_size=0.2)

sentiment_train = sentiment_model["train"].shuffle(seed=42).select([i for i in list(range(3000))])
sentiment_test  = sentiment_model["test"].shuffle(seed=42).select([i for i in list(range(300))])

imdb = load_dataset("imdb")
small_train_dataset = imdb["train"].shuffle(seed=42).select([i for i in list(range(3000))])
small_test_dataset = imdb["test"].shuffle(seed=42).select([i for i in list(range(300))])
print(small_train_dataset[0])
print(sentiment_train[0])

def preprocess_function(examples):
   return tokenizer(examples["text"], truncation=True)

tokenized_train = sentiment_train.map(preprocess_function, batched=True)
tokenized_test  = sentiment_test.map(preprocess_function, batched=True)

# train_dataframe = DataFrame(sentiment_train).dropna()
# train_list      = train_dataframe["lyrics"].tolist()
# tokenized_train = tokenizer(train_list) 

# test_dataframe = DataFrame(sentiment_test).dropna()
# test_list      = test_dataframe["lyrics"].tolist()
# tokenized_test = tokenizer(train_list) 

data_collector = DataCollatorWithPadding(tokenizer=tokenizer)

model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

def compute_metrics(eval_pred):
   load_accuracy = load_metric("accuracy")
   load_f1 = load_metric("f1")
  
   logits, labels = eval_pred
   predictions = np.argmax(logits, axis=-1)
   accuracy = load_accuracy.compute(predictions=predictions, references=labels)["accuracy"]
   f1 = load_f1.compute(predictions=predictions, references=labels)["f1"]
   return {"accuracy": accuracy, "f1": f1}

training_args = TrainingArguments(
   output_dir="ssc",
   learning_rate=2e-5,
   per_device_train_batch_size=16,
   per_device_eval_batch_size=16,
   num_train_epochs=2,
   weight_decay=0.01,
   save_strategy="epoch",
   push_to_hub=True,
)
 
trainer = Trainer(
   model=model,
   args=training_args,
   train_dataset=tokenized_train,
   eval_dataset=tokenized_test,
   tokenizer=tokenizer,
   data_collator=data_collector,
   compute_metrics=compute_metrics,
)

trainer.train()
trainer.evaluate()