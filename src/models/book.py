class Book:
    def __init__(self, book_id, title, author, category, publication_year, current_borrower):
        self.book_id = book_id                  # Mã sách (duy nhất)
        self.title = title                # Tên sách
        self.author = author              # Tác giả
        self.category = category          # Thể loại
        self._publication_year = publication_year  # Năm xuất bản (ẩn)
        self._is_available = True         # Trạng thái mượn/trả
        self.borrow_count = 0             # Số lần được mượn
        self.current_borrower = current_borrower or None      # Người đang mượn sách (nếu có)
        
    @property
    def is_available(self):
        return self._is_available
    
    def borrow(self):
        if self._is_available:
            self._is_available = False
            self.borrow_count += 1
            return True
        return False
    
    def return_book(self):
        self._is_available = True
    
    def __str__(self):
        if self._is_available:
            availability = "Available"
        else:
            availability = "Borrowed"
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Category: {self.category}, Year: {self._publication_year}, Status: {availability}, Borrowed: {self.borrow_count} times"