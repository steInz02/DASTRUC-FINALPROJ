# ==============================
# STAINES PART
# DISPLAY AND NAVIGATION
# ==============================

def print_movie(movie):

    print("-------------------------")
    print("Movie ID:", movie.movie_id)
    print("Title:", movie.title)
    print("Actor:", movie.actor)
    print("Screen Time:", movie.screen_time)
    print("Popularity Rating:", movie.rating)
    print("Director:", movie.director)
    print("Genre:", movie.genre)
    print("Release Year:", movie.release_year)


# DISPLAY MOVIES FROM HEAD TO TAIL
def display_forward(self):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    temp = self.head

    print("\nMOVIE PLAYLIST FORWARD:")

    while True:

        print_movie(temp)
        temp = temp.next

        # STOP IF BACK TO HEAD
        if temp == self.head:
            break


# DISPLAY MOVIES FROM TAIL TO HEAD
def display_reverse(self):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    temp = self.tail

    print("\nMOVIE PLAYLIST REVERSE:")

    while True:

        print_movie(temp)
        temp = temp.prev

        # STOP IF BACK TO TAIL
        if temp == self.tail:
            break


# DISPLAY CURRENT MOVIE
def current_movie(self):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    print("\nCURRENT MOVIE:")
    print_movie(self.current)


# MOVE TO NEXT MOVIE
def next_movie(self):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    self.current = self.current.next

    print("\nNOW PLAYING:")
    print_movie(self.current)


# MOVE TO PREVIOUS MOVIE
def previous_movie(self):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    self.current = self.current.prev

    print("\nNOW PLAYING:")
    print_movie(self.current)
