# File: tests/test_music_library_integration.py
from lib.music_library import MusicLibrary
from lib.track import Track


def test_music_library_integration():
    library = MusicLibrary()
    track_1 = Track("Running Up That Hill", "Kate Bush")
    track_2 = Track("Queencard", "G-IDLE")
    library.add(track_1)
    library.add(track_2)
    assert library.all() == [track_1, track_2]

def test_searches_title():
    library = MusicLibrary()
    track_1 = Track("Running Up That Hill", "Kate Bush")
    track_2 = Track("Queencard", "G-IDLE")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Running Up That Hill") == [track_1]

def test_search_for_track_by_word():
    library = MusicLibrary()
    track_1 = Track("Running Up That Hill", "Kate Bush")
    track_2 = Track("Queencard", "G-IDLE")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Running") == [track_1]
# ...
