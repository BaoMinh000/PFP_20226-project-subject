from src.services.file_io import save_to_file, load_from_file
from src.models.book import Book
from src.configs.config import DATA_BOOKS_FILE

class LibraryManager:
    def __init__(self):
        self.books = []

    # def add_book(self, books):
    #     # self.books.append(book)
    #     print("Adding a new book...")
    #     title  = input("Enter book title: ")
    #     author = input("Enter book author: ")
    #     category = input("Enter book category: ")
    #     publication_year = input("Enter publication year: ")
    #     book_id = len(books) + 1  # Simple way to generate a unique book ID
    #     new_book = Book(book_id, title, author, category, publication_year, None)
    #     books.append(new_book)
    #     if save_to_file(books, DATA_BOOKS_FILE):
    #         print("Data saved successfully.")
    #         print(f"Book '{title}' added successfully with ID {book_id}.")
    #     else:
    #         print("Failed to save data.")
        
    def display_statistics(self, books):
        print("Library Statistics:")
        print(books)
        # for book in books:1
        #     for i in book:
        #         print(f"book[{i}]: {book[i]}")

    # def remove_book(self, book_id):
    #     self.books = [b for b in self.books if b.book_id != book_id]

    # def search_by_title(self, keyword):
    #     return [b for b in self.books if keyword.lower() in b.title.lower()]

    # def borrow_book(self, book_id):
    #     for b in self.books:
    #         if b.book_id == book_id:
    #             return b.borrow()
    #     return False

    # def return_book(self, book_id):
    #     for b in self.books:
    #         if b.book_id == book_id:
    #             b.return_book()
    #             return True
    #     return False
