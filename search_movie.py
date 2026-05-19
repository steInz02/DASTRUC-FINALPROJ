# ==============================
# SEARCH FUNCTIONS
# ==============================

from display_navigation import print_movie

def search_by_title(playlist, title):
    if playlist.is_empty():
        print("Playlist is empty.")
        return

    temp = playlist.head

    while True:
        if temp.title.lower() == title.lower():
            print("\nMOVIE FOUND:")
            print_movie(temp)
            return

        temp = temp.next

        if temp == playlist.head:
            break

    print("Movie not found.")


def search_by_actor(playlist, actor):
    if playlist.is_empty():
        print("Playlist is empty.")
        return

    temp = playlist.head
    found = False

    while True:
        if actor.lower() in temp.actor.lower():
            if found == False:
                print("\nMOVIES FOUND:")

            print_movie(temp)
            found = True

        temp = temp.next

        if temp == playlist.head:
            break

    if found == False:
        print("No movies found for that actor.")
