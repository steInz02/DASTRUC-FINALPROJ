# ==============================
# MOVIE NODE / CLASS
# ==============================
# THIS FILE IS FOR CREATING ONE MOVIE NODE.
# EACH MOVIE STORES DETAILS AND HAS NEXT AND PREV POINTERS.

class MovieNode:
    def __init__(self, movie_id, title, actor, screen_time, rating, director, genre, release_year):
        self.movie_id = movie_id
        self.title = title
        self.actor = actor
        self.screen_time = screen_time
        self.rating = rating
        self.director = director
        self.genre = genre
        self.release_year = release_year

        # POINTERS FOR CIRCULAR DOUBLY LINKED LIST
        self.next = None
        self.prev = None
