#!/usr/bin/env python3

import tkinter as tk
from api.genius import GeniusAPI

class Gui(tk.Tk):
    def __init__(self, api_obj : GeniusAPI) -> None:
        super().__init__()

        self.geniusapi = api_obj

        self.title("SSC")
        self.geometry("600x400")
        self.minsize(340, 200)

        self.label = tk.Label(self, text="song sentiment comparer", font=(None, 14))
        self.label.pack(fill=tk.X, pady=(64, 22))

        self.entry = tk.Entry(self, justify="center", width=52)
        self.entry.pack(fill=tk.NONE)

        self.search = tk.Button(self, text="search", command=self.search)
        self.search.pack(fill=tk.NONE)

        self.output = tk.Label(self, text="", font=(None, 14))
        self.output.pack(fill=tk.NONE, pady=(60, 12))

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    def search(self) -> None:
        searchinput = self.entry.get()
        artistsongobj = self.geniusapi.get_artistsong_obj_from_search(searchinput)[0]
        lyrics = self.geniusapi.get_lyrics_from_song(songtitle=artistsongobj["title"], artistname=artistsongobj["artist"])

        self.output["text"] = lyrics

if __name__ == "__main__":
    root = Gui()
    root.mainloop()

# https://raw.githubusercontent.com/Dvlv/Tkinter-By-Example/master/Tkinter-By-Example.pdf