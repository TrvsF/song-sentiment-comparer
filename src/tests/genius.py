from lyricsgenius import Genius
import json

keyjson = json.load(open("keys.json", "r"))
key = keyjson["genius-access"]

genius = Genius(key)

songsearch = genius.search_songs("gee beach boy")
with open('dict.txt', 'w') as file:
     file.write(json.dumps(songsearch))

for hit in songsearch["hits"]:
    result = hit["result"]
    print(result["title"])
    print(result["artist_names"])
    print("---")


# artist = genius.search_artist("Ween", max_songs=3, sort="title")
# print(artist.songs)