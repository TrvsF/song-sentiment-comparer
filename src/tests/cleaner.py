import re

with open("lyricsout.txt", "r") as file:
    lyrics = file.read()

print(lyrics)

# get all after word 'lyrics'
# remove all chars in [] (and the braces)
# if word contains Embed remove all after \w is satisfied

m = re.search(r"(?<=Lyrics)[^*]*", lyrics)
m2 = re.search(r"[^*]*(?=Embed)", m.group(0))
print(m2.group(0))