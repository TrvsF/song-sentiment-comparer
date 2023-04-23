from transformers import pipeline, DistilBertModel

model = DistilBertModel.from_pretrained("./ssc/checkpoint-376/")
sentiment_model = pipeline(model=model)
sentiment_model(["I love this move", "This movie sucks!"])