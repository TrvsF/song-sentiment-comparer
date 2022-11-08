#!/usr/bin/env python3

from api.genius import GeniusAPI

def main() -> None:
    print("starting song sentiment comparer")
    api = GeniusAPI()

    searchinput = input()
    artistsongobj = api.get_artistsong_obj_from_search(searchinput)[0]
    lyrics = api.get_lyrics_from_song(songtitle=artistsongobj["title"], artistname=artistsongobj["artist"])

    print(f"{lyrics}")    

if __name__ == "__main__":
    main()