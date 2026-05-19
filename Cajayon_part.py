# ==============================
# CAJAYON PART
# ADD MOVIE FUNCTIONS
# ==============================

# ADD MOVIE AT BEGINNING
def add_beginning(self, new_movie):

    # CHECK DUPLICATE
    if self.is_duplicate(new_movie.title):
        print("Movie title already exists.")
        return

    # EMPTY LIST
    if self.head is None:

        self.head = new_movie
        self.tail = new_movie

        # POINT TO ITSELF
        new_movie.next = self.head
        new_movie.prev = self.head

        self.current = self.head

    else:

        temp = self.head

        # FIND LAST NODE
        while temp.next != self.head:
            temp = temp.next

        # LAST NODE POINTS TO NEW MOVIE
        temp.next = new_movie

        # NEW MOVIE POINTS TO OLD HEAD
        new_movie.next = self.head

        # OLD HEAD POINTS BACK TO NEW MOVIE
        self.head.prev = new_movie

        # NEW MOVIE POINTS BACK TO LAST NODE
        new_movie.prev = temp

        # MOVE HEAD
        self.head = new_movie

        # UPDATE TAIL
        self.tail = temp

    print("Movie added successfully.")


# ADD MOVIE AT END
def add_end(self, new_movie):

    # CHECK DUPLICATE
    if self.is_duplicate(new_movie.title):
        print("Movie title already exists.")
        return

    # EMPTY LIST
    if self.head is None:

        self.head = new_movie
        self.tail = new_movie

        new_movie.next = self.head
        new_movie.prev = self.head

        self.current = self.head

    else:

        temp = self.head

        # FIND LAST NODE
        while temp.next != self.head:
            temp = temp.next

        # INSERT AT END
        temp.next = new_movie

        # NEW NODE POINTS TO HEAD
        new_movie.next = self.head

        # NEW NODE POINTS BACK TO OLD LAST NODE
        new_movie.prev = temp

        # HEAD POINTS BACK TO NEW LAST NODE
        self.head.prev = new_movie

        # UPDATE TAIL
        self.tail = new_movie

    print("Movie added successfully.")


# ADD MOVIE AT POSITION
def add_position(self, new_movie, position):

    # INVALID POSITION
    if position < 1:
        print("Invalid position.")
        return

    # CHECK DUPLICATE
    if self.is_duplicate(new_movie.title):
        print("Movie title already exists.")
        return

    # EMPTY LIST
    if self.head is None:

        if position == 1:

            self.head = new_movie
            self.tail = new_movie

            new_movie.next = self.head
            new_movie.prev = self.head

            self.current = self.head

            print("Movie added successfully.")

        else:
            print("Position out of range.")

        return

    # INSERT AT BEGINNING
    if position == 1:
        add_beginning(self, new_movie)
        return

    total = self.count_movies()

    # INSERT AT END
    if position == total + 1:
        add_end(self, new_movie)
        return

    # CHECK IF POSITION IS TOO FAR
    if position > total + 1:
        print("Position out of range.")
        return

    temp = self.head
    count = 1

    # MOVE TO POSITION
    while count < position - 1 and temp.next != self.head:
        temp = temp.next
        count += 1

    # INSERT NODE
    new_movie.next = temp.next
    new_movie.prev = temp

    temp.next.prev = new_movie
    temp.next = new_movie

    print("Movie added successfully.")
