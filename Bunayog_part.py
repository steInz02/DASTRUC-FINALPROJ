# ==============================
# BUNAYOG PART
# MOVIE NODE, PLAYLIST, AND PRELOADED MOVIES
# ==============================

class MovieNode:

    def __init__(self, movie_id, title, actor, screen_time,
                 rating, director, genre, release_year):

        self.movie_id = movie_id
        self.title = title
        self.actor = actor
        self.screen_time = screen_time
        self.rating = rating
        self.director = director
        self.genre = genre
        self.release_year = release_year

        self.next = None
        self.prev = None


class MoviePlaylist:

    def __init__(self):

        self.head = None
        self.tail = None
        self.current = None

    # CHECK IF PLAYLIST IS EMPTY
    def is_empty(self):

        if self.head is None:
            return True
        else:
            return False

    # CHECK DUPLICATE TITLE
    def is_duplicate(self, title):

        if self.head is None:
            return False

        temp = self.head

        while True:

            if temp.title.lower() == title.lower():
                return True

            temp = temp.next

            if temp == self.head:
                break

        return False

    # COUNT ALL MOVIES
    def count_movies(self):

        if self.head is None:
            return 0

        count = 0
        temp = self.head

        while True:

            count += 1
            temp = temp.next

            if temp == self.head:
                break

        return count


def preload_movies():

    playlist = MoviePlaylist()

    movie1 = MovieNode(
        "M01",
        "Titanic",
        "Leonardo DiCaprio and Kate Winslet",
        194,
        8.0,
        "James Cameron",
        "Drama, History, Romance",
        1997
    )

    movie2 = MovieNode(
        "M02",
        "The Greatest Showman",
        "Hugh Jackman, Zac Efron, Michelle Williams, Zendaya",
        105,
        7.5,
        "Michael Gracey",
        "Drama, Musical, Biography",
        2017
    )

    movie3 = MovieNode(
        "M03",
        "Girl, Boy, Bakla, Tomboy",
        "Vice Ganda, Maricel Soriano, Joey Marquez",
        103,
        6.2,
        "Wenn V. Deramas",
        "Comedy, Parody, Drama",
        2013
    )

    movie4 = MovieNode(
        "M04",
        "Sisterakas",
        "Vice Ganda, Kris Aquino, Ai-Ai delas Alas",
        110,
        5.4,
        "Wenn V. Deramas",
        "Comedy, Drama",
        2012
    )

    movie5 = MovieNode(
        "M05",
        "Almost Us",
        "Fyang Smith and JM Ibarra",
        102,
        7.1,
        "Dan Villegas",
        "Romantic, Comedy, Drama",
        2026
    )

    # LINKING THE NODES
    movie1.next = movie2
    movie2.prev = movie1

    movie2.next = movie3
    movie3.prev = movie2

    movie3.next = movie4
    movie4.prev = movie3

    movie4.next = movie5
    movie5.prev = movie4

    # MAKE IT CIRCULAR
    movie5.next = movie1
    movie1.prev = movie5

    # SET POINTERS
    playlist.head = movie1
    playlist.tail = movie5
    playlist.current = movie1

    return playlist
