class Book:
    def __init__(self, book_id, title, author, category, publication_year,
                 is_available=True, borrow_count=0, current_borrower=None):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self._publication_year = publication_year
        self._is_available = is_available
        self.borrow_count = borrow_count
        # self.current_borrower = current_borrower   # None nếu chưa ai mượn
        
    @property
    def is_available(self):
        return self._is_available
    
    def borrow(self, borrower_info):
        if self._is_available:
            self._is_available = False
            self.borrow_count += 1
            # self.current_borrower = borrower_info
            return True
        return False
    
    def get_borrow_count(self):
        return self.borrow_count
    
    def return_book(self):
        self._is_available = True
        # self.current_borrower = None        # xóa người mượn
    
    def __str__(self):
        status = "Available" if self._is_available else "Borrowed"
        # borrower = self.current_borrower if self.current_borrower else "None"

        return (
            f"Book ID: {self.book_id}, "
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Category: {self.category}, "
            f"Year: {self._publication_year}, "
            f"Status: {status}, "
            f"Borrow count: {self.borrow_count}, "
            # f"Borrower: {borrower}"
        )
