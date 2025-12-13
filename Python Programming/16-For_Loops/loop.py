''' loops in pyhton
sometimes a programmer wants to execute a group of statement a certain number of times. this can be done using loop.
based on this loops further classified into following types.for loop, while loop, nested loops.'''

# For loop 
'''
for loops can iterate over a sequence of iterable objects in python. Iterating over sequence is nothing but iterating over strings,
lists, tuples, sets and dictionaries. 
'''

# name = "vivek"

# for i in name:
#     print(i)
#     if(i == "i"):
#         print("this is something special.")

# list = [ 1, 2 , 3]

# for i in list:
#     print(i)
#     if(i> 1):
#         print("this is greater than 1.")

# fruits = [ "apple", "banana", "jackfruit","kiwi"]
# for i in fruits:
#     print(i)
    
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print("Sum is:", total)


def sum_of_n_numbers(n):
   return n * (n + 1) // 2

n = int(input("Enter the number: "))

print("The sum of first",n, "numbers is:",sum_of_n_numbers(n))

n = int(input("Enter the number: "))
total = 0

for i in  range (1, n + 1):
   total += i 
   
print("The sum of first",n, "numbers is:",total)



































