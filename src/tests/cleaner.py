import re

with open("Strai.txt", "r") as file:
    lyrics = file.read()

# get all after word 'lyrics'
# remove all chars in [] (and the braces)
# if word contains Embed remove all after \w is satisfied

lyrics = lyrics.replace("You might also like", "")

# remove the top 'Lyrics'
lyrics = (re.search(r"(?<=Lyrics)[^*]*", lyrics)).group(0)
# remove the footer embed
m2 = re.search(r"[\d]*(?=Embed)\w*", lyrics)
# remove '[]'s
lyrics = lyrics.replace(m2.group(0), "")
m3 = re.findall(r"\[.*?\]", lyrics)

# [lyrics.replace(group, "") for group in m3]
for word in m3:
    lyrics = lyrics.replace(word, "")

# lyrics = (re.search(r"^\n", lyrics)).group(0)

print(lyrics)