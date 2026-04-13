# Variables
a = 15
b = 4

# Arithmetic Operators:

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)

# Relational Operators:

a = 33
b = 33

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)

# Logical Operators:

a = 10
b = 22

print(a and b)
print(a or b)
print(not a )
print(not b)


# Bitwise Operator:

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)


# Assignment Operator:
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)


b <<= a
# b <<= a : b = b << a
# b <<= a -> multiply b by 2^a (b * 2^a)
print(b)



m = int(input("Enter the number: "))
n = m

n <<= m 
print(n)

s = int(input("Enter the number: "))
d = s 

d >>= s 
# d >>= s : d = d >> s
# d >>= s : d / 2^s
print(d)



# Identity Operators:

#  IS
a = 10 
b = a
print(a == b)
print(a is b)
'''
Here, a = 10 and b = a so, b = 10 aswell
a is b says that same values located at same memory locations'''


a = [1,2,3]
b = [1,2,3]
print(a is b)
'''
Here, it means that both a and b shares the same values but a and b are different memory locations in which the same values are assigned.
a ──► [1,2,3]   (Object 1)

b ──► [1,2,3]   (Object 2)      
'''

a = [1, 2, 3]
b = a

print(a is b)  # True
'''
a ─┐
   ├──► [1,2,3]
b ─┘
'''

# is not -> 👉 Checks if two variables are NOT the same object (memory)

a = [1,2,3]
b = [1,2,3]
print(a is not b)
# a ──► [1,2,3]   (Object 1)
# b ──► [1,2,3]   (Object 2)

a = [1,2,3]
b = a
print(a is not b)
# a ─┐
#    ├──► [1,2,3]
# b ─┘


# Membership Operator:

# in            True if value is found in the sequence
# not in        True if value is not found in the sequence

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")