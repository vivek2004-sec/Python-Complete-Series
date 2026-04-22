

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lst)

fruits = ['Mango', 'Apple', 'Watermelon', 'Grapes', 'Banana', 'Kiwi']
print(fruits)

vue = ['Vivek', 2, 'James', (1, 2, 3), {'vivek':1, 'sujal':2}]
print(vue)

# . Using list() Constructor

a = list((1, 2, 3, 'vivek', 'sujal'))
print(a)

ms = {'mango': 23, 'grapes':12}
a = list(ms)
print(a)

#  Creating List with Repeated Elements

a = [2] * 5
b = [3] * 8

print(a, b)


'''
Accessing List Elements
Elements in a list are accessed using indexing. Python uses zero-based indexing, meaning a[0] represents the first element.
Negative indexing is also supported, where -1 accesses the last element.'''


a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])