# ---------- Imports ----------
# from asyncio.log import logger 
from src.ui.menu_handler import handle_menu_choice
from src.ui.menu import show_menu
from src.configs.config import DATA_BOOKS_FILE
from src.services.file_io import save_to_file, load_from_file
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
    # print("list students: ", students)
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if not handle_menu_choice(choice=choice, books = books):
            break
# ---------- Program Entry Point ----------
if __name__ == "__main__":
    main()
    