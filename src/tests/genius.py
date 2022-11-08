from lyricsgenius import Genius
import json

keyjson = json.load(open("keys.json", "r"))
key = keyjson["genius-access"]

genius = Genius(key)

search_term = input("search...")

songsearch = genius.search_songs(search_term)
hits = songsearch["hits"]

c = 0
for hit in hits:
    result = hit["result"]
    print("{0} : {1} by {2}".format(c, result["title"], result["artist_names"]))
    c += 1

i = int(input("select input"))

songtitle = hits[i]["result"]["title"]
artistname = hits[i]["result"]["artist_names"]

songobj = genius.search_song(songtitle, artist=artistname)
print(songobj.lyrics)

# artist = genius.search_artist("Ween", max_songs=3, sort="title")
# print(artist.songs)