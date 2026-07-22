class Library:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
library = Library("New York Public Library.")
print(library.name)

book1 = Book("Haary Potter Series", "J.K. Rowling")
book2 = Book("The Hobbit Series", "J.R. R.  Tolkein")
print(book1.title)
print(book1.author)
print(book2.title)
print(book2.author)