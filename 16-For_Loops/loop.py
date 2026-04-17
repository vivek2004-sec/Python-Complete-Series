''' Loops in pyhton:
sometimes a programmer wants to execute a group of statement a certain number of times. this can be done using loop.
based on this loops further classified into following types.for loop, while loop, nested loops.
Loops in Python are used to repeat actions efficiently. 
The main types are For loops (counting through items) and While loops (based on conditions).
'''

# For loop 
'''
for loops can iterate over a sequence of iterable objects in python. Iterating over sequence is nothing but iterating over strings,
lists, tuples, sets and dictionaries. 
'''




# For String:

name = "vivek"

for ch in name:
   print(ch)



# For List:

ls = ['Mango', 'Kiwi', 'Banana', 'Watermelon', 'Grapes']

for fruits in ls:
   print(fruits)


# For Tuple:

tup = (1, 2, 3, 4, 5)

for num in tup:
   print(num)

   
# For Set:

s = {1, 2, 3, 4}

for num in s:
   print(num)


# For Dictionary:


dic = {'a': 1, 'b': 2, 'c': 3}

for v in dic:
   print(v)
# shows only keys

for value in dic.values():
   print(value)
# Shows only values.

# for key in dic.keys():
#    print(key)


# for items in dic:
#    print(dic[items])


# for key, value in dic.items():
#    print(key, value)







