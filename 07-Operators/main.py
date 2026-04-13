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
