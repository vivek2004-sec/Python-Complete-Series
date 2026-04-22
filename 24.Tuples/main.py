tup = (1,5, 7, "green", True)
print(type(tup), tup)

print(tup[1])
print(tup[0:3])
print(tup[1:4])
print(tup[:-2])
print(tup[0:4])
print(tup[:-4])
print(tup[:-2])

n = int(input("Enter the number:"))
if n  in tup:
    print(n," is present in tup.")
else:
    print(n," is not present in tup.")

a = (1, 2, 3, 4, [1, 2, 3, 4, 5], {'vivek':1, 'sujal': 3}, 'vivek', 'usual')
print(a)


tup1 = (2, 3, 4, 5)
tup2 = ('vivek', 'kamble')
tup3 = tup1 + tup2
print(tup3)


tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])


tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) 
print(b) 
print(c)

fru = ("mango", "apple", "orange", 'pineapple')
*a, b, c = fru
print(a)
print(b)
print(c)


cars = ('nissan', 'swift', 'thar', 'bmw', 'sierra', 'mercedes', 'vokswagen')
a, b, *c, d = cars
print(a)
print(b)
print(c)
print(d)


# Reversing a Tuple

# Most common and Pythonic way to reverse a tuple is by using slicing with a step of -1, here is how we can do it:

num = (2, 3, 4, 5, 6, 7, 8)
print(num[::-1])


t = (1, 2, 3, 4, 5)  
# Reverse the tuple using the built-in reversed() function and convert it back to a tuple
rev = tuple(reversed(t))
print(rev)