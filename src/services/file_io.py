# from src.models.student_model import Student
from services import book
from src.models.book import Book

def save_to_file(books, filename):
    print("Saving book data...")
    print("Please wait...")
    try:
        with open(filename, 'w') as f:
            for book in books:
                # print("Writing book:", book)
                line = (
                    f"{book.book_id},"
                    f"{book.title},"
                    f"{book.author},"
                    f"{book.category},"
                    f"{book._publication_year},"
                    f"{book.is_available},"
                    f"{book.borrow_count},"
                    # f"{book.current_borrower if book.current_borrower else 'None'}\n"
                )
                # print("Line to write:", line)
                f.write(line)
        return True
    except FileNotFoundError:
        print("File not found. Unable to save data.")
        return False
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

def load_from_file(filename):
    books = []
    print("Loading book data...")
    print("Please wait...")
    try:
        with open(filename, 'r') as f:
            for line in f:
                data_in_line = line.strip().split(',')
                book_id = data_in_line[0]
                title = data_in_line[1]
                author = data_in_line[2]
                category = data_in_line[3]
                year = data_in_line[4]
                is_available = data_in_line[5].lower() == 'true'
                borrow_count = int(data_in_line[6])
                # current_borrower = data_in_line[7] if len(data_in_line) > 7 else None
                book = Book(
                    book_id,
                    title,
                    author,
                    category,
                    year,
                    is_available,
                    borrow_count,
                    # current_borrower
                )
                books.append(book)
    except FileNotFoundError:
        print("File not found. Starting with an empty book list.")
        books = []
    except Exception as e:
        print(f"Error loading from file: {e}")
    
    return books
