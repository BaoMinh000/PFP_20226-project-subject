
from time import time
from src.services.file_io import load_from_file
from src.configs.config import DATA_BOOKS_FILE
from src.models import book
from src.utils.screen import clear_screen
from src.services.book import add_book, return_book, update_book, delete_book, display_books, search_books, update_book, borrow_book
from src.models.library_manage import LibraryManager
from src.configs.config import DATA_BOOKS_FILE
library_manager = LibraryManager()
def handle_menu_choice(choice, books):
    try:
        books = load_from_file(DATA_BOOKS_FILE)
    except FileNotFoundError:
        books = []
        
    if choice == "1":
        add_book(books)
        # library_manager.add_book(books)
    elif choice == "2":
        update_book(books)

    elif choice == "3":
        delete_book(books)
    elif choice =="4":
        # library_manager.display_statistics(books)
        display_books(books)
    elif choice == "5":
        search_books(books)
    elif choice == "6":
        borrow_book(books)
    elif choice == "7":
        return_book(books)
    elif choice == "0":
        print("Goodbye!")
        clear_screen() 
        return False
    elif choice.lower() == "r":
        print("Reloading data from file...")
        time.sleep(1)
        
        clear_screen()
        return "RELOAD"

    else:
        print("Invalid choice! Try again.")

    return True
