def search_by_(type_search_name, arr, type_search_value):
    Found = False
    new_list = []
    print(f"Searching by :{type_search_name}", type_search_value)
    for s in arr:
        if s.book_id == type_search_value:
            new_list.append(s)
            Found = True
    if not Found:
        print(f"No book found with this {type_search_name}.")
    return new_list

def advanced_search(books, book_id=None , name=None,title=None, author=None, category=None, publication_year=None):
    results = books
    
    if book_id:
        results = search_by_("book_id", results, book_id)
    
    if name:
        results = search_by_("name", results, name)
        
    if title:
        results = search_by_("title", results, title)
    
    if author:
        results = search_by_("author", results, author)
        
    if category:
        results = search_by_("category", results, category)
        
    if publication_year:
        results = search_by_("publication_year", results, publication_year)
        
    return results
