import csv
import nltk
import string
import matplotlib.pyplot as plt

from textblob            import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from numpy               import random

plt.rcParams.update({'font.size': 7})

MAXCOUNT = 20000

def get_genres():
    genrecount = {}
    c = 0
    reader = csv.DictReader(open('data/id_tags.csv', 'r', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)
    for item in reader:
        for tag in item["tags"].split(","):
            if tag in genrecount:
                genrecount[tag] += 1
            else:
                genrecount[tag] = 1
        c += 1
        if c > MAXCOUNT:
            break

    return genrecount

def get_artist():
    artistcount = {}
    c = 0
    reader = csv.DictReader(open('data/id_information.csv', 'r', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)
    for item in reader:
        if item["artist"] in artistcount:
            artistcount[item["artist"]] += 1
        else:
            artistcount[item["artist"]] = 1
        c += 1
        if c > MAXCOUNT:
            break

    return artistcount

def get_wordcount():
    wordcount = {}
    c = 0
    reader = csv.DictReader(open('data/dataset-full.csv', 'r', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)
    for item in reader:
        for tag in item["lyrics"].split(" "):
            if tag == "":
                continue
            tag = tag.lower()
            tag = tag.translate(str.maketrans('', '', string.punctuation))
            if tag in wordcount:
                wordcount[tag] += 1
            else:
                wordcount[tag] = 1
        c += 1
        if c > MAXCOUNT:
            break

    return wordcount

def get_random_sample():
    sents = []
    c = 0
    reader = csv.reader(open('data/dataset-full.csv', 'r', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)
    readerlist = list(reader)
    while (c < MAXCOUNT):
        i = random.randint(2, len(readerlist))
        tag = readerlist[i][2]
        tag = tag.lower()
        tag = tag.translate(str.maketrans('', '', string.punctuation))
        sents.append(tag)
        c += 1

    return sents

def get_random_sample_id():
    sents = {}
    c = 0
    reader = csv.reader(open('data/dataset-full.csv', 'r', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)
    readerlist = list(reader)
    while (c < MAXCOUNT):
        i = random.randint(2, len(readerlist))
        id = readerlist[i][0]
        tag = readerlist[i][2]
        tag = tag.lower()
        tag = tag.translate(str.maketrans('', '', string.punctuation))
        sents[id] = tag
        c += 1

    return sents

def draw_data(d, r = 10):
    listkeys = list(d.keys())[-r:]
    listvalues = list(d.values())[-r:]

    plt.bar(range(r), listvalues, align='center')
    plt.xticks(range(r), listkeys)
    plt.show()

sentlist = get_random_sample_id()
sentilist = []
for id, sent in sentlist.items():
    sentiment = TextBlob(sent)
    polarity = sentiment.sentiment.polarity
    subjectivity = sentiment.sentiment.subjectivity

    sent          = TextBlob(sent, analyzer = NaiveBayesAnalyzer())
    classification= sent.sentiment.classification
    positive      = sent.sentiment.p_pos
    negative      = sent.sentiment.p_neg
    
    print(polarity,subjectivity,classification,positive,negative)
    sentilist.append([id, classification, positive, negative, sent])

with open('sentiment.csv', 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["id", "classification", "positive", "negative", "lyrics"])
    for row in sentilist:
        writer.writerow(row)

'''
# get nouns
wordlist = get_random_sample()
wordstr  = " ".join(word for word in wordlist)

blob = TextBlob(wordstr)
dict = blob.np_counts
sorteddict = { key:val for key, val in sorted(dict.items(), key=lambda item: item[1]) }
print(sorteddict)
draw_data(sorteddict)
'''
