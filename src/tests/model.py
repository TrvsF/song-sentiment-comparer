from transformers import pipeline, DistilBertModel

sentiment_model = pipeline(model="trvsf/ssc")
print(sentiment_model(["I love this move", "This movie sucks!"]))