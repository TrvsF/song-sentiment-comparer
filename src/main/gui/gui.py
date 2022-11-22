#!/usr/bin/env python3

import tkinter as tk
import util.regularexpression as reutil

from api.genius import GeniusAPI

class Gui(tk.Tk):
    def __init__(self, apiobject : GeniusAPI) -> None:
        super().__init__()

        # assign genius api
        self.genius_api = apiobject

        # set window vars
        self.title("SSC")
        self.geometry("600x400")
        self.minsize(600, 400)

        # define fonts
        self.header_font = ("System", 22, "bold")
        self.default_font = ("System", 12)

        # safe close for model
        self.protocol("WM_DELETE_WINDOW", self.safe_destroy)

        # menu frame
        self.menu_frame = tk.Frame(self,
            width = 600,
            height = 400,
            bg = "lightgrey"
        )

        # menu gui items
        self.title = tk.Label(self.menu_frame,
            text = "song sentiment comparer",
            bg = "lightgrey",
            fg = "black",
            font = self.header_font
        )
        self.search_bar = tk.Entry(self.menu_frame,
            bg = "white",
            fg = "black",
            width = 52,
            font = self.default_font
        )
        self.recommended_one = tk.Label(self.menu_frame,
            text="ween bananas and blow",
            bg = "white",
            fg = "black",
            width = 52,
            anchor = "w",
            font = self.default_font
        )
        self.recommended_two = tk.Label(self.menu_frame,
            text="talking heads im not in love",
            bg = "white",
            fg = "black",
            width = 52,
            anchor = "w",
            font = self.default_font
        )
        self.recommended_thr = tk.Label(self.menu_frame,
            text="travis side",
            bg = "white",
            fg = "black",
            width = 52,
            anchor = "w",
            font = self.default_font
        )
        self.output_box = tk.Label(self.menu_frame,
            text = "this is an output\nyipeeee",
            bg = "lightgrey",
            fg = "black",
            font = self.default_font
        )

        self.recommended_list = [
            self.recommended_one,
            self.recommended_two,
            self.recommended_thr
        ]

        # pack all items
        self.menu_frame.pack(fill=tk.BOTH, expand=1)
        self.title.pack(fill=tk.X, pady=(32, 28))
        self.search_bar.pack(fill=tk.NONE, pady=(2, 0))

        for label in self.recommended_list:
            label.pack(fill=tk.NONE)

        self.output_box.pack(fill=tk.BOTH, pady=(22, 12))

        # binds
        self.bind("<Return>", lambda event: self.search(event, searchtext=self.search_bar.get()))
        self.bind("<Alt_L>", lambda event: self.getsuggested(event, searchtext=self.search_bar.get()))
        # for each recommended
        self.recommended_one.bind("<Button-1>", lambda event: self.search(event, searchtext=self.recommended_one["text"]))
        self.recommended_two.bind("<Button-1>", lambda event: self.search(event, searchtext=self.recommended_two["text"]))
        self.recommended_thr.bind("<Button-1>", lambda event: self.search(event, searchtext=self.recommended_thr["text"]))

        # focus search bar
        self.search_bar.focus()

    def getsuggested(self, event = None, searchtext = "") -> None:
        for i, artistsongobj in enumerate(self.genius_api.get_artistsong_obj_from_search(searchtext, size_limit=3)):
            self.recommended_list[i]["text"] = f"{artistsongobj['title']} - {artistsongobj['artist']}"
        self.update()

    def search(self, event = None, searchtext = "") -> None:
        artistsongobj = None

        # searchinput = self.search_bar.get() if searchtext == "" else searchtext
        artistsongobj = self.genius_api.get_artistsong_obj_from_search(searchtext)[0]

        if artistsongobj == None:
            print("artist obj was none")
            return None

        lyrics = self.genius_api.get_lyrics_from_song(songtitle=artistsongobj["title"], artistname=artistsongobj["artist"])

        self.output_box["text"] = reutil.clean_lyrics(lyrics) if lyrics != "" else "timed out"

    def safe_destroy(self) -> None:
        # check if model is running & stop
        print("deading...")
        self.destroy()

if __name__ == "__main__":
    root = Gui()
    root.mainloop()

# https://raw.githubusercontent.com/Dvlv/Tkinter-By-Example/master/Tkinter-By-Example.pdf