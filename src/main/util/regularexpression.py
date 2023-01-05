#!/usr/bin/env python3

import re

def clean_lyrics(lyrics : str) -> str:
    # remove string seemingly random inserted into some lyric pulls
    lyrics = lyrics.replace("You might also like", "")

    # remove the top 'Lyrics'
    lyrics = (re.search(r"(?<=Lyrics)[^*]*", lyrics)).group(0)

    # remove the footer embed
    lyrics = re.sub(r"[\d]*(?=Embed)\w*", "", lyrics)

    # remove '[]'s
    lyrics = re.sub(r"\[.*?\]", "", lyrics)

    # clean empty newlines
    lyrics = re.sub(r"(?<=\n)\s+", "", lyrics)

    return lyrics