from datavisualiser      import get_lyric_id_pairs
from textblob            import TextBlob
from textblob            import Blobber
from textblob.sentiments import NaiveBayesAnalyzer

import csv

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def main() -> None:
    sentdict = get_lyric_id_pairs()
    sentilist = []
    tb = Blobber(analyzer = NaiveBayesAnalyzer())
    for id, lyrics in sentdict.items():

        sent          = tb(lyrics)
        classification= sent.sentiment.classification
        positive      = sent.sentiment.p_pos
        negative      = sent.sentiment.p_neg

        classification = 1 if sent.sentiment.classification == "pos" else 0

        if (not isEnglish(lyrics)):
            continue

        sentilist.append([lyrics, classification])

    with open('data/sentiment.csv', 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["lyrics", "label"])
        for row in sentilist:
            writer.writerow(row)

if __name__ == "__main__":
    main()