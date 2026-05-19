# ==============================
# ADD MOVIE FUNCTIONS
# ==============================

def add_beginning(playlist, new_movie):
    if playlist.is_duplicate(new_movie.title):
        print("Movie title already exists.")
        return

    if playlist.is_empty():
        playlist.head = new_movie
        playlist.tail = new_movie
        playlist.current = new_movie

        new_movie.next = new_movie
        new_movie.prev = new_movie

    else:
        new_movie.next = playlist.head
        new_movie.prev = playlist.tail

        playlist.head.prev = new_movie
        playlist.tail.next = new_movie

        playlist.head = new_movie

    print("Movie added at the beginning successfully.")


def add_end(playlist, new_movie):
    if playlist.is_duplicate(new_movie.title):
        print("Movie title already exists.")
        return

    if playlist.is_empty():
        playlist.head = new_movie
        playlist.tail = new_movie
        playlist.current = new_movie

        new_movie.next = new_movie
        new_movie.prev = new_movie

    else:
        new_movie.prev = playlist.tail
        new_movie.next = playlist.head

        playlist.tail.next = new_movie
        playlist.head.prev = new_movie

        playlist.tail = new_movie

    print("Movie added at the end successfully.")


def add_position(playlist, new_movie, position):
    if position < 1:
        print("Invalid position.")
        return

    if playlist.is_duplicate(new_movie.title):
        print("Movie title already exists.")
        return

    size = playlist.count_movies()

    if position > size + 1:
        print("Position out of range.")
        return

    if position == 1:
        add_beginning(playlist, new_movie)
        return

    if position == size + 1:
        add_end(playlist, new_movie)
        return

    temp = playlist.head
    count = 1

    while count < position - 1:
        temp = temp.next
        count += 1

    new_movie.next = temp.next
    new_movie.prev = temp

    temp.next.prev = new_movie
    temp.next = new_movie

    print("Movie added at position", position, "successfully.")
