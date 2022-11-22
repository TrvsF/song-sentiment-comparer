#!/usr/bin/env python3

from api.genius import GeniusAPI
from gui.gui import Gui

def main() -> None:
    print("starting song sentiment comparer...")
    api = GeniusAPI()
    gui = Gui(api)

    gui.mainloop()

if __name__ == "__main__":
    main()