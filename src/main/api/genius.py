#!/usr/bin/env python3

from lyricsgenius import Genius
from requests.exceptions import HTTPError, Timeout
import json

class GeniusAPI:
    def __init__(self) -> None:
        keyjson = json.load(
            open("api/keys.json", "r")
        )
        key = keyjson["genius-access"]
        self.genius = Genius(key)

    def get_artistsong_obj_from_search(self, search_term = "") -> list:
        hits = self.get_hits_from_search(search_term)
        artistsongobj = self.get_artistsong_obj_from_hits(hits)
        return artistsongobj

    def get_hits_from_search(self, search_term = "") -> list:
        try:
            searchresult = self.genius.search_songs(search_term)
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

    def get_artistsong_obj_from_hits(self, hits_obj = None) -> list:
        if hits_obj == None:
            return []

        artistsongobj = []
        for hit in hits_obj:
            result = hit["result"]
            hitobj = {}

            hitobj["title"] = result["title"]
            hitobj["artist"] = result["artist_names"]

            artistsongobj.append(hitobj)

        return artistsongobj