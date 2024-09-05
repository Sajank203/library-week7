#main.py
from book import book
from library import library

# create some book objects
book1 = book("python programming", "jhon smith")
book2 = book("data science essentials", "alice johnson")
book3 = book("web development basics", "boob wilson")

#create a library
library = library()

# add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

#borrow and return books
print(library.borrow_book("python programming")) #borrow book 1
print(library.borrow_book("python programming")) #already borrowed
print(library.borrow_book("python programming")) #return book1
print(library.borrow_book("python programming")) #not currently borrowed

#count how many books are currently borrowed
print(f"number of borrowed books: {library.borrowed_count}")