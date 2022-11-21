#!/usr/bin/env python3

from api.genius import GeniusAPI
from gui.gui import Gui

def main() -> None:
    print("starting song sentiment comparer")
    api = GeniusAPI()
    gui = Gui(api)

    gui.mainloop()

    # searchinput = input()
    # artistsongobj = api.get_artistsong_obj_from_search(searchinput)[0]
    # lyrics = api.get_lyrics_from_song(songtitle=artistsongobj["title"], artistname=artistsongobj["artist"])

    # print(f"{lyrics}")  

    # with open(f"{lyrics[:5]}.txt", "w", encoding="utf-8") as file:
    #     file.write(lyrics)

if __name__ == "__main__":
    main()