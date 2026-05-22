# Encoding & Decoding

import random
import string

code = input("Enter the code: ")

def random_chars():
    return ''.join(random.choices(string.ascii_letters, k=3))

def random_digits():
    return ''.join(random.choices(string.digits, k=3))

def encode(code):
    if len(code) >= 3:
        code = code[1:] + code[0]          
        code = random_chars() + random_digits() + code + random_digits() + random_chars()  
    else:
        code = code[::-1]                   
        code = random_chars() + random_digits() + code + random_digits() + random_chars()  
    return code

def decode(code):
    code = code[6:-6]
    if len(code) >= 3:
        code = code[-1] + code[:-1]
    else:
        code = code[::-1]
    return code

encoded = encode(code)        
decoded = decode(code)  

print(f"Original → {code}")
print(f"Encoded  → {encoded}")
print(f"Decoded  → {decoded}")