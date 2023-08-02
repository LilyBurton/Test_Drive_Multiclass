# File: lib/diary.py
import math

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        total = 0
        for word in self._entries:
            total += word.count_words()
        return total

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time with wpm of 0")
        else:
            word_count = self.count_words()
        return math.ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_that_reader_can_read = wpm * minutes
        most_readable = None
        longest_read = 0
        for entry in self._entries: 
            if entry.count_words() <=  words_that_reader_can_read:
                if entry.count_words() > longest_read:
                    most_readable = entry
                    longest_read = entry.count_words()
        return most_readable


