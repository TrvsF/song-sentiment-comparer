import csv
import functools

reader = csv.DictReader(open('data/id_lang.csv', 'r', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)

@functools.lru_cache
def get_filetxt(filename):
    with open(f'data/lyrics/{filename}.txt', 'r', encoding='utf-8') as file:
        txt = file.read().replace('\n', ' ')
        return txt

dictlist = []
c = 0

for item in reader:
    if (item['lang'] == 'en'):
        lyrics = get_filetxt(item['id']).replace('"', '')
        item['lyrics'] = lyrics
        dictlist.append(item)
        c+=1

    if (c == 25000):
        break

keys = dictlist[0].keys()
with open('dataset.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dictlist)