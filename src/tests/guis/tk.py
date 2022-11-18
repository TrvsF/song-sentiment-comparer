import tkinter as tk

class Search(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("SSC")
        self.geometry("600x400")
        self.minsize(340, 200)

        self.label = tk.Label(self, text="song sentiment comparer", font=(None, 14))
        self.label.pack(fill=tk.X, pady=(64, 22))

        self.entry = tk.Entry(self, justify="center", width=52)
        self.entry.pack(fill=tk.NONE)

        self.search = tk.Button(self, text="search", command=self.search)
        self.search.pack(fill=tk.NONE)

        self.output = tk.Label(self, text="aaa", font=(None, 14))
        self.output.pack(fill=tk.NONE, pady=(60, 12))

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    def search(self) -> None:
        txt = self.entry.get()
        self.output["text"] = txt

if __name__ == "__main__":
    root = Search()
    root.mainloop()