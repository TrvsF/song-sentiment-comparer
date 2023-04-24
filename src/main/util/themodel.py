from transformers import pipeline

sentiment_model = pipeline(model="trvsf/ssc")

def GetSentiment(lyrics, debug=False):
    anal = sentiment_model(lyrics)[0]
    if (debug):
        print(anal)
    # 1 for pos 0 for neg
    confidence = round(anal["score"] * 100, 1)
    if anal["label"] == "LABEL_1":
        return f"Positive @{confidence}%"
    else:
        return f"Negative @{confidence}%"