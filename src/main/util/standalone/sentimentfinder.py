from datavisualiser      import get_random_sample_id
from textblob            import TextBlob
from textblob            import Blobber
from textblob.sentiments import NaiveBayesAnalyzer

import csv

def main() -> None:
    sentlist = get_random_sample_id()
    sentilist = []
    tb = Blobber(analyzer = NaiveBayesAnalyzer())
    for id, sent in sentlist.items():
        sentiment = TextBlob(sent)
        polarity = sentiment.sentiment.polarity
        subjectivity = sentiment.sentiment.subjectivity

        sent          = tb(sent)
        classification= sent.sentiment.classification
        positive      = sent.sentiment.p_pos
        negative      = sent.sentiment.p_neg
        
        print(polarity,subjectivity,classification,positive,negative)
        sentilist.append([id, classification, positive, negative, sent])

    with open('data/sentiment.csv', 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["id", "classification", "positive", "negative", "lyrics"])
        for row in sentilist:
            writer.writerow(row)

if __name__ == "__main__":
    main()