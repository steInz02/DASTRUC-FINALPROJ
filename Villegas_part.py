# ==============================
# VILLEGAS PART
# DELETE AND UPDATE FUNCTIONS
# ==============================

# DELETE MOVIE
def delete_movie(self):

    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    title = input("Enter movie title to delete: ")

    temp = self.head

    while True:

        # IF MOVIE IS FOUND
        if temp.title.lower() == title.lower():

            # CONFIRMATION
            confirm = input("Delete this movie? (yes/no): ").lower()

            if confirm != "yes":
                print("Delete cancelled.")
                return

            # IF ONLY ONE MOVIE
            if temp.next == self.head and temp.prev == self.head:
                self.head = None
                self.current = None

            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

                # IF DELETING THE HEAD
                if temp == self.head:
                    self.head = temp.next

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
def update_movie(self):
    
    # CHECK IF PLAYLIST IS EMPTY
    if self.head is None:
        print("Playlist is empty.")
        return

    title = input("Enter movie title to update: ")

    temp = self.head

    while True:

        # IF MOVIE IS FOUND
        if temp.title.lower() == title.lower():

            print("\nEnter new movie details")

            temp.title = input("New title: ")
            temp.actor = input("New actor: ")
            temp.time = input("New screen time: ")
            temp.director = input("New director: ")
            temp.genre = input("New genre: ")
            temp.year = input("New release year: ")
            
            # VALIDATED RATING INPUT (1.0 - 10.0)
            while True:
                try:
                    rating = float(input("New popularity rating (1.0 - 10.0): "))
                    if 1.0 <= rating <= 10.0:
                        temp.rating = rating
                        break
                    else:
                        print("Rating must be between 1.0 and 10.0 only.")
                except ValueError:
                    print("Invalid input. Please enter a number (example: 8, 6.7, 9.75).")

            print("Movie updated successfully!")
            return

        temp = temp.next

        # STOP IF BACK TO HEAD
        if temp == self.head:
            break

    print("Movie not found.")
