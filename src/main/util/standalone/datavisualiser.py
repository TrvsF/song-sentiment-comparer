import csv
import string
import matplotlib.pyplot as plt

from numpy               import random

plt.rcParams.update({'font.size': 7})

MAXCOUNT = 50000

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

def get_lyric_id_pairs():
    sents = {}
    reader = csv.DictReader(open('data/dataset-full.csv', 'r', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)
    for item in reader:
        lyrics = item["lyrics"]
        lyrics = lyrics.lower()
        lyrics = lyrics.translate(str.maketrans('', '', string.punctuation))
        id = item["id"]
        sents[id] = lyrics
    return sents

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

def get_sentiment_dict():
    sentimentcount = {"pos" : 0, "neg" : 0}
    reader = csv.DictReader(open('data/sentiment.csv', 'r', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)
    for item in reader:
        tag = item["classification"]
        sentimentcount[tag] += 1
        
    return sentimentcount

def draw_data_pie(d):
    listkeys = list(d.keys())
    listvalues = list(d.values())

    fig, ax = plt.subplots()
    ax.pie(listvalues, labels=listkeys, autopct='%1.1f%%')
    plt.show()

def draw_data_bar(d, r = 10):
    listkeys = list(d.keys())[-r:]
    listvalues = list(d.values())[-r:]

    plt.bar(range(r), listvalues, align='center')
    plt.xticks(range(r), listkeys)
    plt.show()

draw_data_pie(get_sentiment_dict())