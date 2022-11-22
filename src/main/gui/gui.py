#!/usr/bin/env python3

import tkinter as tk

from api.genius import GeniusAPI

class Gui(tk.Tk):
    def __init__(self, apiobject : GeniusAPI) -> None:
        super().__init__()

        self.genius_api = apiobject

        self.title("SSC")
        self.geometry("600x400")
        self.minsize(600, 400)

        self.header_font = ("System", 22, "bold")
        self.default_font = ("System", 12)

        self.protocol("WM_DELETE_WINDOW", self.safe_destroy)

        self.main_frame = tk.Frame(self,
            width = 600,
            height = 400,
            bg = "lightgrey"
        )

        self.title = tk.Label(self.main_frame,
            text = "song sentiment comparer",
            bg = "lightgrey",
            fg = "black",
            font = self.header_font
        )
        self.search_bar = tk.Entry(self.main_frame,
            bg = "white",
            fg = "black",
            width = 52,
            font = self.default_font
        )
        # self.search_button = tk.Button(self.main_frame,
        #     text = "search",
        #     bg = "lightgrey",
        #     fg = "black",
        #     font = self.default_font,
        #     command = self.search
        # )
        self.recommended_one = tk.Label(self.main_frame,
            text="ween bananas and blow",
            bg = "lightgrey",
            fg = "black",
            font = self.default_font
        )
        self.recommended_two = tk.Label(self.main_frame,
            text="talking heads im not in love",
            bg = "lightgrey",
            fg = "black",
            font = self.default_font
        )
        self.recommended_thr = tk.Label(self.main_frame,
            text="travis side",
            bg = "lightgrey",
            fg = "black",
            font = self.default_font
        )
        self.output_box = tk.Label(self.main_frame,
            text = "this is an output\nyipeeee",
            bg = "lightgrey",
            fg = "black",
            font = self.default_font
        )

        self.main_frame.pack        (fill=tk.BOTH, expand=1)

        self.title.pack             (fill=tk.X, pady=(32, 28))
        self.search_bar.pack        (fill=tk.NONE)
        self.recommended_one.pack   (fill=tk.NONE)
        self.recommended_two.pack   (fill=tk.NONE)
        self.recommended_thr.pack   (fill=tk.NONE)
        # self.search_button.pack (fill=tk.NONE)
        self.output_box.pack        (fill=tk.BOTH, pady=(22, 12))

        self.recommended_one.bind("<Button-1>", lambda eff: self.search(eff, search_text=self.recommended_one["text"]))
        self.recommended_two.bind("<Button-1>", lambda eff: self.search(eff, search_text=self.recommended_two["text"]))
        self.recommended_thr.bind("<Button-1>", lambda eff: self.search(eff, search_text=self.recommended_thr["text"]))
        self.bind("<Return>", self.search)

        self.search_bar.focus()

    def search(self, event = None, search_text = "") -> None:
        artistsongobj = None

        if search_text == "":
            searchinput = self.search_bar.get()
            artistsongobj = self.genius_api.get_artistsong_obj_from_search(searchinput)[0]
        else:
            artistsongobj = self.genius_api.get_artistsong_obj_from_search(search_text)[0]

        if artistsongobj == None:
            print("artist obj was none")
            return

        lyrics = self.genius_api.get_lyrics_from_song(songtitle=artistsongobj["title"], artistname=artistsongobj["artist"])

        self.output_box["text"] = lyrics

    def safe_destroy(self) -> None:
        # check if model is running & stop
        print("deading...")
        self.destroy()

if __name__ == "__main__":
    root = Gui()
    root.mainloop()

# https://raw.githubusercontent.com/Dvlv/Tkinter-By-Example/master/Tkinter-By-Example.pdf