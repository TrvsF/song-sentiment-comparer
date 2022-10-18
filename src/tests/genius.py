from lyricsgenius import Genius
import json

keyjson = json.load(open("keys.json", "r"))
key = keyjson["genius-access"]

genius = Genius(key)
artist = genius.search_artist("Ween", max_songs=3, sort="title")
print(artist.songs)