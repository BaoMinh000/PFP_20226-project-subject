from src.services.file_io import save_to_file
from src.models.book import Book
from src.configs.config import DATA_BOOKS_FILE

def add_book(books):
    # self.books.append(book)
    print("Adding a new book...")
    book_id = len(books) + 1  # Simple ID generation
    # Check for unique book_id
    for i, book in enumerate(books):
        if str(int(i)+1) != str(book.book_id):
            book_id = int(i)+1
            break
    
    while True:
        title  = input("Enter book title: ")
        author = input("Enter book author: ")
        category = input("Enter book category: ")
        publication_year = input("Enter publication year: ")
            
        if book_id and title and author and category and publication_year : 
            break
        else:
            cancel = input("Do you want cancel adding book? (y/n): ")
            if cancel.lower() == 'y':
                return
            print("All fields are required. Please try again.")
    
    # Create and add the new book
    new_book = Book(book_id, title, author, category, publication_year, None)
    books.append(new_book)
    
    # Save to file
    print("Saving data...")
    if save_to_file(books, DATA_BOOKS_FILE):
        print("Data saved successfully.")
        print(f"Book '{title}' added successfully with ID {book_id}.")
    else:
        print("Failed to save data.")

def update_book(library_manager, books):
    pass

def delete_book(books):
    print("Deleting a book...")
    book_id = input("Enter the Book ID to delete: ")
    if book_id.strip() == "":
        print("Book ID cannot be empty.")
        return
    for book in books:
        if str(book.book_id) == book_id:
            books.remove(book)
            save_to_file(books, DATA_BOOKS_FILE)
            print(f"Book ID {book_id} deleted successfully.")
            return
    print(f"Book ID {book_id} not found.")

            
def display_books(books):
    if not books:
        print("No books in the system.")
        return

    for i, book in enumerate(books):
        print(f"i: {i} - {book}")
    
    print("===== BOOK LIST =====")

    header = (
        f"| {'ID':<12}"
        f"| {'Title':<24}"
        f"| {'Author':<24}"
        f"| {'Category':<24}"
        f"| {'Year':<10}"
        f"| {'Status':<13}"
        f"| {'Borrowed':<10} |"
    )

    line = "+" + "-" * (len(header) - 2) + "+"

    print(line)
    print(header)
    print(line)

    for book in books:
        print(
            f"| {book.book_id:<12}"
            f"| {book.title:<24}"
            f"| {book.author:<24}"
            f"| {book.category:<24}"
            f"| {book._publication_year:<10}"
            f"| {'Available' if book.is_available else 'Borrowed':<13}"
            f"| {book.borrow_count:<10} |"
        )

    print(line)


def search_books(books):
    pass
