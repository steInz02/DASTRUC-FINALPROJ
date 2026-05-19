# ==============================
# VILLEGAS PART
# DELETE AND UPDATE FUNCTIONS
# ==============================

# DELETE MOVIE
def delete_movie(self, title):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    temp = self.head

    while True:

        # IF MOVIE IS FOUND
        if temp.title.lower() == title.lower():

            # IF ONLY ONE MOVIE
            if temp.next == self.head and temp.prev == self.head:
                self.head = None
                self.tail = None
                self.current = None

            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

                # IF DELETING THE HEAD
                if temp == self.head:
                    self.head = temp.next

                # IF DELETING THE TAIL
                if temp == self.tail:
                    self.tail = temp.prev

                # UPDATE CURRENT POINTER
                if temp == self.current:
                    self.current = temp.next

            print("Movie deleted successfully!")
            return

        temp = temp.next

        # STOP IF BACK TO HEAD
        if temp == self.head:
            break

    print("Movie not found.")


# UPDATE MOVIE
def update_movie(self, title):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    temp = self.head

    while True:

        # IF MOVIE IS FOUND
        if temp.title.lower() == title.lower():

            print("\nEnter new movie details")

            temp.movie_id = input("New movie ID: ")
            temp.title = input("New title: ")
            temp.actor = input("New actor: ")
            temp.screen_time = input("New screen time: ")
            temp.rating = input("New popularity rating: ")
            temp.director = input("New director: ")
            temp.genre = input("New genre: ")
            temp.release_year = input("New release year: ")

            print("Movie updated successfully!")
            return

        temp = temp.next

        # STOP IF BACK TO HEAD
        if temp == self.head:
            break

    print("Movie not found.")
