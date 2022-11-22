import re

with open("Ocean.txt", "r") as file:
    lyrics = file.read()

# get all after word 'lyrics'
# remove all chars in [] (and the braces)
# if word contains Embed remove all after \w is satisfied

# remove string seemingly random inserted into some lyric pulls
lyrics = lyrics.replace("You might also like", "")

# remove the top 'Lyrics'
lyrics = (re.search(r"(?<=Lyrics)[^*]*", lyrics)).group(0)

# remove the footer embed
lyrics = re.sub(r"[\d]*(?=Embed)\w*", "", lyrics)

# remove '[]'s
lyrics = re.sub(r"\[.*?\]", "", lyrics)

# clean newlines
lyrics = re.sub(r"(?<=\n)\s+", "", lyrics)

print(lyrics)