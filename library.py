# library. py
from book import book
class library:
    def __init__(self):
        self.books = []     
        self.borrowed_count = 0
    def add_book(self, book):
        self.books.append(book)
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    self.borrowed_count += 1
                    return f"successfully borrowed: {title}"
                else:
                    return f" {title} is already borrowed."    
        return f"{title} not found in the library." 
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.return_book():
                    self.borrowed_count = 1
                    return f"successsfully returned: {title}"
                else:
                    return f"{title} is not currently borrowed."
 
        return f"{title} not found in the library."