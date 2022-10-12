from lyricsgenius import Genius

genius = Genius('4zmULjlrE6SHJ2oli_GHxS-IvzaCP_tzuB7OfWSQaSEtd06fHCoOfXKHkQ_zCpLA')
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)