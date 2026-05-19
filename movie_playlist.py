# ==============================
# MOVIE PLAYLIST CLASS
# ==============================
# THIS FILE CONTAINS THE MAIN PLAYLIST STRUCTURE.
# IT ALSO HAS BASIC CHECKING FUNCTIONS USED BY OTHER FEATURES.

class MoviePlaylist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    # CHECK IF PLAYLIST IS EMPTY
    def is_empty(self):
        return self.head is None

    # CHECK IF THE TITLE ALREADY EXISTS
    def is_duplicate(self, title):
        if self.is_empty():
            return False

        temp = self.head

        while True:
            if temp.title.lower() == title.lower():
                return True

            temp = temp.next

            if temp == self.head:
                break

        return False

    # COUNT HOW MANY MOVIES ARE INSIDE THE PLAYLIST
    def count_movies(self):
        if self.is_empty():
            return 0

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        return count
