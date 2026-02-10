# ---------- Imports ----------
# from asyncio.log import logger 
from src.ui.menu_handler import handle_menu_choice
from src.ui.menu import show_menu
from src.configs.config import DATA_BOOKS_FILE
from src.services.file_io import load_from_file
# Import necessary modules


# ---------- Data Structure ----------
data_books = DATA_BOOKS_FILE
# ---------- GPA Calculation ----------
# logger.info("Program started")
def main():
    try:
        books = load_from_file(data_books)
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        books = []
    
    print("Welcome to the Student Management System!")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if not handle_menu_choice(choice=choice, books = books):
            break
# ---------- Program Entry Point ----------
if __name__ == "__main__":
    main()
    
    
# Update sort_books() to accept sorting condition and order as parameters
# Modify sort_books() to return the sorted book list instead of only printing messages

# Update list_all_books() / display_books() to call sort_books(books, "id", "asc")
# Ensure books are sorted by ID in ascending order before displaying

# Update list_most_borrowed_books() to use sort_books()
# Sort books by borrow_count in descending order and display top 5 most borrowed books

# Modify handle_menu_choice() to call statistics menu from menu.py
# Remove direct statistics menu printing from handle_menu_choice()

# Update data/books.txt to include borrower information
# Ensure consistent data format for all book records

# Add time.sleep(1) before exiting the program
# Allow users time to read messages before the program closes
