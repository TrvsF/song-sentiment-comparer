from transformers import AutoTokenizer, TrainingArguments, Trainer, DataCollatorWithPadding, AutoModelForSequenceClassification
from datasets import load_dataset, load_metric
# from pandas import DataFrame

import numpy as np

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

sentiment_dataset_obj = load_dataset("csv", data_files="data/sentiment.csv")
sentiment_data        = sentiment_dataset_obj["train"].train_test_split(test_size=0.2)

sentiment_train = sentiment_data["train"].shuffle(seed=42)
sentiment_test  = sentiment_data["test"].shuffle(seed=42)
train_len = len(sentiment_train)
test_len = len(sentiment_test)

print(f"processing with sizes [{train_len}:{test_len}]")

def preprocess_function(examples):
   return tokenizer(examples["text"], truncation=True)

tokenized_train = sentiment_train.map(preprocess_function, batched=True)
tokenized_test  = sentiment_test.map(preprocess_function, batched=True)

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