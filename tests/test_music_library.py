from lib.music_library import MusicLibrary

def test_initially_have_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []

def test_initially_have_empty_list():
    music_library = MusicLibrary()
    assert music_library.search_by_title("Walking") == []


