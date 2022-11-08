from lyricsgenius import Genius
from requests.exceptions import HTTPError, Timeout
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

def get_hits_from_search(search_term = "") -> list:
    try:
        searchresult = genius.search_songs(search_term)
    except HTTPError as e:
        print(f"bad repsonce, code '{e.errno}' @get_hits_from_search")
        return []
    except Timeout as t:
        print(f"timed out @get_hits_from_search")
        return []

    if "hits" in searchresult:
        return searchresult["hits"]
    else:
        return []

def get_artistsong_obj_from_hits(hits_obj = None) -> list:
    if hits_obj == None:
        return []

    artistsongobj = []
    for hit in hits_obj:
        result = hit["result"]
        hitobj = {}

        hitobj["title"] = result["title"]
        hitobj["artist"] = result["artist_names"]

        artistsongobj.append(hits_obj)

    return artistsongobj