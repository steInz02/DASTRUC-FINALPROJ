# ==============================
# DELETE AND UPDATE FUNCTIONS
# ==============================

def delete_movie(playlist, title):
    if playlist.is_empty():
        print("Playlist is empty.")
        return

    temp = playlist.head

    while True:
        if temp.title.lower() == title.lower():

            if playlist.head == playlist.tail:
                playlist.head = None
                playlist.tail = None
                playlist.current = None

            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

                if temp == playlist.head:
                    playlist.head = temp.next

                if temp == playlist.tail:
                    playlist.tail = temp.prev

                if temp == playlist.current:
                    playlist.current = temp.next

            print("Movie deleted successfully.")
            return

        temp = temp.next

        if temp == playlist.head:
            break

    print("Movie not found.")


def update_movie(playlist, title):
    if playlist.is_empty():
        print("Playlist is empty.")
        return

    temp = playlist.head

    while True:
        if temp.title.lower() == title.lower():
            print("\nEnter new movie details:")

            temp.movie_id = input("Movie ID: ")
            temp.title = input("Title: ")
            temp.actor = input("Actor: ")
            temp.screen_time = input("Screen Time: ")
            temp.rating = input("Rating: ")
            temp.director = input("Director: ")
            temp.genre = input("Genre: ")
            temp.release_year = input("Release Year: ")

            print("Movie updated successfully.")
            return

        temp = temp.next

        if temp == playlist.head:
            break

    print("Movie not found.")
