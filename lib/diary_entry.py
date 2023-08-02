# File: lib/diary_entry.py

class DiaryEntry:
    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        self._stop_off_point = 0
        

    def count_words(self):
        
        return len(self.contents.split())
        
        

    def reading_time(self, wpm):
        return len(self.contents.split()) / wpm

    def reading_chunk(self, wpm, minutes):
        readable_chunks = wpm * minutes
        words = self.contents.split()
        start_point = self._stop_off_point
        end_point = self._stop_off_point + readable_chunks
        readable_chunk = " ".join(words[start_point:end_point])
        self._stop_off_point += readable_chunks
        return readable_chunk
