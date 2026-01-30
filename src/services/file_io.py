# from src.models.student_model import Student
from src.models.book import Book

def save_to_file(books, filename):
    print("Saving book data...")
    print("Please wait...")
    
    try:
        with open(filename, 'w') as f:
            for book in books:
                line = f"{book.book_id},{book.title},{book.author},{book.category},{book._publication_year}\n"
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
                
                book = Book(
                    book_id,
                    title,
                    author,
                    category,
                    year,
                    None
                )
                books.append(book)
    except FileNotFoundError:
        print("File not found. Starting with an empty book list.")
        books = []
    except Exception as e:
        print(f"Error loading from file: {e}")
        
    return books
