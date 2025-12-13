# # # Strings
# # '''
# # In python anything that you enclose between single or double Quotation marks is considered
# # as a string. strings are immutable in pyhton. A string is essentially a sequence or array 
# # of characters. Strings are used to represent text data. 
# # '''

name= "Vivek"
apple= "He said, \"he wants to eat an apple.\""

prime= '''hello, 
my name is vivek kamble.
I'm from kolhapur maharashtra.
its glad to see you.'''
print("The name is:", name)
# print(apple)

print(prime)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # throws an error

# For loop 
print("Lets use for loop\n")
for character in name:
    print(character)
print("Lets use for loop\n")
for character in apple:
    print(character)
    
game= "Kamble"

print(game[0])
print(game[1])
print(game[2])
print(game[3])
print(game[4])
print(game[5])

print("\n")
for characters in game:
    print(characters)
    
vue = '''hello, my name is rishi.
I live in Kagal, I have family of 4 members
and I love them so much.'''

print(type(vue))

A = 7.54
print(type(A))


hs = "hello"

print("\n")
for characters in hs:
     print(characters)