from lib.diary_entry import DiaryEntry

def test_contrust_entry_to_get_title_and_contents():
    diary_entry = DiaryEntry("Title 1", "A Contents 2")
    assert diary_entry.title == "Title 1"
    assert diary_entry.contents == "A Contents 2"

def test_count_words_in_entry():
    diary_entry = DiaryEntry("Title 1", "A Contents 2")
    assert diary_entry.count_words() == 3

def test_entries_reading_time():
    diary_entry = DiaryEntry("Title 1", "A Contents 2")
    assert diary_entry.reading_time(3) == 1

def test_reading_chunk():
    diary_entry = DiaryEntry("Title 1", "A Contents 2")
    assert diary_entry.reading_chunk(2, 1) == "A Contents"

def test_reading_chunk_second_half():
    diary_entry = DiaryEntry("Title 1", "A Contents 3 2")
    assert diary_entry.reading_chunk(2, 1) == "A Contents"
    assert diary_entry.reading_chunk(2, 1) == "3 2"