from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_diary_entry_integration():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title 1", "A Contents 2")
    diary_entry2 = DiaryEntry("Title 3", "A Contents 4")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.all() == [diary_entry1, diary_entry2]

def test_count_words_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title 1", "A Contents 2")
    diary_entry2 = DiaryEntry("Title 3", "A Contents 4")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.count_words() == 6

def test_returns_reading_time_from_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title 1", "A Contents 2")
    diary_entry2 = DiaryEntry("Title 3", "A Contents 4")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.reading_time(5) == 2
    
def test_returns_best_entry_reading_time_that_best_fit():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title", "A Contents")
    diary_entry2 = DiaryEntry("Title 3", "A Contents 4")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2, 1) == diary_entry1

def test_returns_best_entry_reading_time_with_one_entry():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title", "A Contents")
    diary.add(diary_entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == diary_entry1

def test_returns_None_if_entries_empty():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title", "A Contents one two three four five six")
    diary.add(diary_entry1)
    assert diary.find_best_entry_for_reading_time(2, 2) == None

def test_returns_longest_readable():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title", "A Contents")
    diary_entry2 = DiaryEntry("Title 3", "A Contents 4")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2, 4) == diary_entry2