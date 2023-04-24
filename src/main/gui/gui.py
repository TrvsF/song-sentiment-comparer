#!/usr/bin/env python3

import tkinter as tk
import util.regularexpression as reutil

from api.genius import GeniusAPI
from util.themodel import GetSentiment

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
            text="ween - bananas and blow",
            bg = "white",
            fg = "black",
            width = 52,
            anchor = "w",
            font = self.default_font
        )
        self.recommended_two = tk.Label(self.menu_frame,
            text="talking heads - im not in love",
            bg = "white",
            fg = "black",
            width = 52,
            anchor = "w",
            font = self.default_font
        )
        self.recommended_thr = tk.Label(self.menu_frame,
            text="travis - side",
            bg = "white",
            fg = "black",
            width = 52,
            anchor = "w",
            font = self.default_font
        )
        self.output_box = tk.Label(self.menu_frame,
            text = "input a song to find more like it\npress 'alt' to autocompleate",
            bg = "lightgrey",
            fg = "black",
            font = self.default_font
        )
        # assign list for recommended labels
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
        # for each recommended, cant do this in a for loop :((
        self.recommended_one.bind("<Button-1>", lambda event: self.search(event, searchtext=self.recommended_one["text"]))
        self.recommended_one.bind("<Enter>",  func=lambda e: self.recommended_one.config(bg="grey"))
        self.recommended_one.bind("<Leave>",  func=lambda e: self.recommended_one.config(bg="white"))
        self.recommended_two.bind("<Button-1>", lambda event: self.search(event, searchtext=self.recommended_two["text"]))
        self.recommended_two.bind("<Enter>",  func=lambda e: self.recommended_two.config(bg="grey"))
        self.recommended_two.bind("<Leave>",  func=lambda e: self.recommended_two.config(bg="white"))
        self.recommended_thr.bind("<Button-1>", lambda event: self.search(event, searchtext=self.recommended_thr["text"]))
        self.recommended_thr.bind("<Enter>",  func=lambda e: self.recommended_thr.config(bg="grey"))
        self.recommended_thr.bind("<Leave>",  func=lambda e: self.recommended_thr.config(bg="white"))

        # focus search bar
        self.search_bar.focus()

    def getsuggested(self, event = None, searchtext = "") -> None:
        # update each recommended label with genius suggestion
        for i, artistsongobj in enumerate(self.genius_api.get_artistsong_obj_from_search(searchtext, size_limit=3)):
            self.recommended_list[i]["text"] = f"{artistsongobj['title']} - {artistsongobj['artist']}"
        # update tkinter bc it gets confused
        self.update()

    def search(self, event = None, searchtext = "", trycount = 0) -> None:
        # check try count
        if trycount > 5:
            self.output_box["text"] = "error finding search from genus"
            return
        # get artistsongobj from search
        artistsongobj = self.genius_api.get_artistsong_obj_from_search(searchtext)[0]
        # if cannot find any results
        if artistsongobj == []:
            print("cannot find any songs")
            self.output_box["text"] = "cannot find any songs from search"
            return None
        # set object var names
        title  = artistsongobj["title"]
        artist = artistsongobj["artist"]
        # set searchbar to text
        self.search_bar.delete(0, tk.END)
        self.search_bar.insert(0, f"{artist} - {title}")
        # get lyrics
        lyrics = self.genius_api.get_lyrics_from_song(songtitle=title, artistname=artist)
        # retry if timed out
        if lyrics == "":
            self.search(searchtext, trycount + 1)
        # cleanup, & output as label
        CleanLyrics = reutil.CleanLyrics(lyrics)
        sentiment_txt = GetSentiment(CleanLyrics, True)
        self.output_box["text"] = sentiment_txt

    def safe_destroy(self) -> None:
        # check if model is running & stop
        print("deading...")
        self.destroy()

if __name__ == "__main__":
    root = Gui()
    root.mainloop()

# https://raw.githubusercontent.com/Dvlv/Tkinter-By-Example/master/Tkinter-By-Example.pdf