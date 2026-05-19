# ==============================
# DISPLAY AND NAVIGATION FUNCTIONS
# ==============================

def print_movie(movie):
    print("-------------------------")
    print("Movie ID:", movie.movie_id)
    print("Title:", movie.title)
    print("Actor:", movie.actor)
    print("Screen Time:", movie.screen_time)
    print("Rating:", movie.rating)
    print("Director:", movie.director)
    print("Genre:", movie.genre)
    print("Release Year:", movie.release_year)


def display_forward(playlist):
    if playlist.is_empty():
        print("Playlist is empty.")
        return

    temp = playlist.head

    print("\nMOVIE PLAYLIST FORWARD:")

    while True:
        print_movie(temp)
        temp = temp.next

        if temp == playlist.head:
            break


def display_reverse(playlist):
    if playlist.is_empty():
        print("Playlist is empty.")
        return

    temp = playlist.tail

    print("\nMOVIE PLAYLIST REVERSE:")

    while True:
        print_movie(temp)
        temp = temp.prev

        if temp == playlist.tail:
            break


def current_movie(playlist):
    if playlist.is_empty():
        print("Playlist is empty.")
        return

    print("\nCURRENT MOVIE:")
    print_movie(playlist.current)


def next_movie(playlist):
    if playlist.is_empty():
        print("Playlist is empty.")
        return

    playlist.current = playlist.current.next
    print("\nNOW PLAYING:")
    print_movie(playlist.current)


def previous_movie(playlist):
    if playlist.is_empty():
        print("Playlist is empty.")
        return

    playlist.current = playlist.current.prev
    print("\nNOW PLAYING:")
    print_movie(playlist.current)
