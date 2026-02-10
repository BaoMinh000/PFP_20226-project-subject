def generate_book_id(books):
    # Tạo danh sách chứa tất cả book_id đang được sử dụng
    used_ids = []

    for book in books:
        used_ids.append(book.book_id)

    # Bắt đầu kiểm tra từ ID = 1
    new_id = 1

    # Nếu ID đã tồn tại thì tăng lên cho đến khi tìm được ID trống
    while new_id in used_ids:
        new_id = new_id + 1

    return new_id
