# Variables and Data Types
'''
what is mean by varibles?

-> Varible is like a container that holds data. Very similar to how our containers in kitchen that holds sugar,
salt etc. Creating a variable is like creating a placeholder in memory and assigning it some values. 
In python it's easy as writing.

# Rules for Naming Variables
To use variables effectively, we must follow Python’s naming rules:


1.Variable names can only contain letters, digits and underscores (_).
2.A variable name cannot start with a digit.
3.Variable names are case-sensitive like myVar and myvar are different.
4.Avoid using Python keywords like if, else, for as variable names.

'''
# a=1
# b=True
# c="Vivek"
# d=None

# Program:

a=1342543537888
print(a)

b="Vivek"
print(b)

Vivek=9879
print(Vivek)

date=2004
print(date)

'''
# Data Types

-> Data type specifies the type of value holds. this is required in programming to do operation
without causing an error. In python, we can print the type of any operator using type function.

Data Types :

1.Text  = str
2.Numeric = int, float, complex
3.Sequence = list, tuple, range
4.Mapping = dict
5.Set = set, fronzset
6.Boolean = bool
7.Binary = bytes, bytearray, memoryview
'''

a=1
b=True
c="Vivek"
d=None
e=9.7
f= 3 + 4j
print("the type of a is ",type(a))
print("the type of b is ",type(b))
print("the type of c is ",type(c))
print("the type of d is ",type(d))
print("the type of e is ",type(e))
print("the type of f is ",type(f))