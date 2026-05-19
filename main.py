# ==============================
# MAIN MENU AND ERROR HANDLING
# ==============================
# THIS FILE CONNECTS ALL OTHER FILES.
# THIS IS ALSO THE PART FOR MENU, INVALID INPUT, AND PROGRAM FLOW.

from movie_node import MovieNode
from movie_playlist import MoviePlaylist

from add_movie import add_beginning, add_end, add_position
from display_navigation import display_forward, display_reverse, current_movie, next_movie, previous_movie
from search_movie import search_by_title, search_by_actor
from delete_update import delete_movie, update_movie


# CREATE MOVIE OBJECT FROM USER INPUT
def create_movie_input():
    print("\nENTER MOVIE DETAILS")

    movie_id = input("Movie ID: ")
    title = input("Title: ")
    actor = input("Actor: ")
    screen_time = input("Screen Time: ")
    rating = input("Rating: ")
    director = input("Director: ")
    genre = input("Genre: ")
    release_year = input("Release Year: ")

    new_movie = MovieNode(movie_id, title, actor, screen_time, rating, director, genre, release_year)

    return new_movie


# DISPLAY ALL MENU OPTIONS
def show_menu():
    print("\n===== MOVIE PLAYLIST MENU =====")
    print("1. Add Movie at Beginning")
    print("2. Add Movie at End")
    print("3. Add Movie at Position")
    print("4. Display Forward")
    print("5. Display Reverse")
    print("6. Current Movie")
    print("7. Next Movie")
    print("8. Previous Movie")
    print("9. Search by Title")
    print("10. Search by Actor")
    print("11. Delete Movie")
    print("12. Update Movie")
    print("13. Exit")


# MAIN PROGRAM
def main():
    playlist = MoviePlaylist()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        # INVALID INPUT HANDLING
        # ISDIGIT CHECKS IF THE INPUT IS A NUMBER
        if choice.isdigit() == False:
            print("Invalid input. Please enter numbers only.")
            continue

        choice = int(choice)

        if choice == 1:
            movie = create_movie_input()
            add_beginning(playlist, movie)

        elif choice == 2:
            movie = create_movie_input()
            add_end(playlist, movie)

        elif choice == 3:
            movie = create_movie_input()
            position = input("Enter position: ")

            if position.isdigit() == False:
                print("Invalid position. Please enter a number only.")
            else:
                add_position(playlist, movie, int(position))

        elif choice == 4:
            display_forward(playlist)

        elif choice == 5:
            display_reverse(playlist)

        elif choice == 6:
            current_movie(playlist)

        elif choice == 7:
            next_movie(playlist)

        elif choice == 8:
            previous_movie(playlist)

        elif choice == 9:
            title = input("Enter title to search: ")
            search_by_title(playlist, title)

        elif choice == 10:
            actor = input("Enter actor to search: ")
            search_by_actor(playlist, actor)

        elif choice == 11:
            title = input("Enter title to delete: ")
            delete_movie(playlist, title)

        elif choice == 12:
            title = input("Enter title to update: ")
            update_movie(playlist, title)

        elif choice == 13:
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please choose from 1 to 13 only.")


# START THE PROGRAM
main()
