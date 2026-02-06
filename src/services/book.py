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
    new_book = Book(book_id, title, author, category, publication_year, None, None)
    books.append(new_book)
    
    # Save to file
    print("Saving data...")
    if save_to_file(books, DATA_BOOKS_FILE):
        print("Data saved successfully.")
        print(f"Book '{title}' added successfully with ID {book_id}.")
    else:
        print("Failed to save data.")

# def update_book(library_manager, books):
#     pass

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

    # for i, book in enumerate(books):
    #     print(f"i: {i} - {book}")
    
    print("=" * 132)
    print("📚 BOOK LIST".center(125))
    print("=" * 132)


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

def update_book(books):
    print("Updating a book...")
    book_id = input("Enter the Book ID to update: ")
    for book in books:
        if str(book.book_id) == book_id:
            new_title = input(f"Enter new title (current: {book.title}): ") or book.title
            new_author = input(f"Enter new author (current: {book.author})): ") or book.author
            new_category = input(f"Enter new category (current: {book.category}): ") or book.category
            new_publication_year = input(f"Enter new publication year (current: {book._publication_year}): ") or book._publication_year
            
            book.title = new_title
            book.author = new_author
            book.category = new_category
            book._publication_year = new_publication_year
            save_to_file(books, DATA_BOOKS_FILE)
            print(f"Book ID {book_id} updated successfully.")
            return
    print(f"Book ID {book_id} not found.")
    
def search_books(books):
    print("Searching for books...")
    print("Enter search criteria (leave blank to skip):")
    print("1. Title/Author/Category keyword")
    title = input("Enter a keyword to search (title): ").strip().lower()
    Author = input("Enter a keyword to search (Author): ").strip().lower()
    Category = input("Enter a keyword to search (Category): ").strip().lower()
    if not title and not Author and not Category:
        print("No search criteria provided.")
        return
    if title:
        print(f"Searching by title containing: {title}")
    if Author:
        print(f"Searching by author containing: {Author}")
    if Category:
        print(f"Searching by category containing: {Category}")
    results = books
    
    for book in results:
        if title:
            new_list = []
            for book in results:
                if title.strip().lower() in book.title.lower():
                    new_list.append(book)
            results = new_list
        if Author:
            new_list = []
            for book in results:
                if Author.strip().lower() in book.author.lower():
                    new_list.append(book)
            results = new_list
        if Category:
            new_list = []
            for book in results:
                if Category.strip().lower() in book.category.lower():
                    new_list.append(book)
            results = new_list
    
    if results:
        print(f"Found {len(results)} matching books:")
        display_books(results)
    else:
        print("No matching books found.")
        
def borrow_book(books):
    print("Borrowing a book...")
    book_id = input("Enter the Book ID to borrow: ")
    for book in books:
        if str(book.book_id) == book_id:
            if book.is_available:
                if book.borrow():
                    print(f"Borrowed book: {book.title}")
                    print("Updating data...")
                    print(f"Data {book}")
                    save_to_file(books, DATA_BOOKS_FILE)
                else:
                    print(f"Failed to borrow book: {book.title}")
                    
            else:
                print(f"Sorry, '{book.title}' is currently not available.")
            return
    print(f"Book ID {book_id} not found.")
    
def return_book(books):
    print("Returning a book...")
    book_id = input("Enter the Book ID to return: ")
    for book in books:
        if str(book.book_id) == book_id:
            if not book.is_available:
                book.return_book()
                save_to_file(books, DATA_BOOKS_FILE)
                print(f"You have successfully returned '{book.title}'.")
            else:
                print(f"'{book.title}' was not borrowed.")
            return
    print(f"Book ID {book_id} not found.")
    
def list_borrowed_books(books):
    print("Listing borrowed books...")
    borrowed_books = [book for book in books if not book.is_available]
    if borrowed_books:
        display_books(borrowed_books)
    else:
        print("No books are currently borrowed.")
        
def list_most_borrowed_books(books):
    print("Listing most borrowed books...")
    sorted_books = sorted(books, key=lambda b: b.borrow_count, reverse=True)
    display_books(sorted_books[:5])  # Display top 5 most borrowed books