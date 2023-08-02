from lib.track import Track

def test_search_track_and_get_title_and_artist():
    track = Track("Running Up That Hill", "Kate Bush")
    assert track.title == "Running Up That Hill"
    assert track.artist == "Kate Bush"

def test_format_title_and_artist():
    track = Track("Running Up That Hill", "Kate Bush")
    assert track.format() == "Running Up That Hill by Kate Bush"