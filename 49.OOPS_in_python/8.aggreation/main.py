class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        return [f"{book.title} and {book.author}" for book in self.books]
 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
library = Library("New York Public Library.")
print(library.name)

book1 = Book("Haary Potter Series", "J.K. Rowling")
book2 = Book("The Hobbit Series", "J.R. R.  Tolkein")
book3 = Book("IT", "stephen king")
book4 = Book("gunaho ka devata", "divykumar bharati")
# del book1
print(book1.title)
print(book1.author)
print(book2.title)
print(book2.author)
print(book3.title)
print(book3.author)
print(book4.title)
print(book4.author)



library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
print(library.books)

print(library.name)
print(library.list_books())