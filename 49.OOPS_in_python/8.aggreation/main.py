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


# Code to demonstrate Aggregation

# Salary class with the public method 
# annual_salary()
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12)+self.bonus


# EmployeeOne class with public method
# total_sal()
class EmployeeOne:

    # Here the salary parameter reflects
    # upon the object of Salary class we
    # will pass as parameter later
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age

        # initializing the sal parameter
        self.agg_salary = sal   # Aggregation

    def total_sal(self):
        return self.agg_salary.annual_salary()

# Here we are creating an object 
# of the Salary class
# in which we are passing the 
# required parameters
salary = Salary(10000, 1500)

# Now we are passing the same 
# salary object we created
# earlier as a parameter to 
# EmployeeOne class
emp = EmployeeOne('Geek', 25, salary)

print(emp.total_sal())



class author:
    def __init__(self, name):
        self.name = name
        
class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        

author1 = author("George Orwell")
print(author1.name)
book1 =book("Time", author1)
print(book1.author.name)
        