# ==============================
# PASCUA PART
# SEARCH FUNCTIONS
# ==============================

from Staines_part import print_movie


# SEARCH BY TITLE FUNCTION
def search_by_title(self, title):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    temp = self.head
    found = False

    while True:

        # PARTIAL SEARCH MATCH
        # EXAMPLE: "TITAN" CAN FIND "TITANIC"
        if title.lower() in temp.title.lower():

            if found == False:
                print("\nMovie Found!")

            print_movie(temp)
            found = True

        temp = temp.next

        # STOP IF BACK TO HEAD
        if temp == self.head:
            break

    if found == False:
        print("Movie not found!")


# SEARCH BY ACTOR FUNCTION
def search_by_actor(self, actor):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    temp = self.head
    found = False

    while True:

        # PARTIAL SEARCH MATCH
        # EXAMPLE: "VICE" CAN FIND "VICE GANDA"
        if actor.lower() in temp.actor.lower():

            if found == False:
                print("\nMovies Found:")

            print_movie(temp)
            found = True

        temp = temp.next

        # STOP IF BACK TO HEAD
        if temp == self.head:
            break

    if found == False:
        print("No movies found!")
