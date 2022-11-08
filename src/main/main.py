#!/usr/bin/env python3

from api.genius import GeniusAPI

def main() -> None:
    print("starting song sentiment comparer")
    api = GeniusAPI()
    for thing in api.get_artistsong_obj_from_search("hotel room"):
        print(thing)

if __name__ == "__main__":
    main()