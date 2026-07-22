class Library:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
library = Library("New York Public Library.")
print(library.name)

book = Book("Haary Potter Series", "J.K. Rowling")
print(book.title)
print(book.author)