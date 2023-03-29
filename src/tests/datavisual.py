import csv
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 7})

MAXCOUNT = 5000000

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

def get_words():
    wordcount = {}
    c = 0
    reader = csv.DictReader(open('data/dataset-full.csv', 'r', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)
    for item in reader:
        for tag in item["lyrics"].split(" "):
            if tag == "":
                continue
            tag = tag.lower()
            if tag in wordcount:
                wordcount[tag] += 1
            else:
                wordcount[tag] = 1
        c += 1
        if c > MAXCOUNT:
            break

    print(wordcount)
    return wordcount


# culleddict = { key:val for key, val in genrecount.items() if val > 5 }
sorteddict = { key:val for key, val in sorted(get_words().items(), key=lambda item: item[1]) }

MAXDATAPOINTS = 30

listkeys = list(sorteddict)[-MAXDATAPOINTS:]
print(listkeys)
listvalues = list(sorteddict.values())[-MAXDATAPOINTS:]
print(listvalues)

plt.bar(range(MAXDATAPOINTS), listvalues, align='center')
plt.xticks(range(MAXDATAPOINTS), listkeys)
plt.show()