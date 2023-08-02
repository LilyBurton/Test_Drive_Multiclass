from lib.diary import Diary
import pytest

def test_empty_diary_entries():
    diary = Diary()
    assert diary.all() == []

def test_initially_word_count_zero():
    diary = Diary()
    assert diary.count_words() == 0

def test_initially_raise_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(0)
    assert str(err.value) == "Cannot calculate reading time with wpm of 0"
