# Credit Card Validator Programm

sum_odd_digits = 0
sum_even_digits = 0

total = 0

# step 1

credit_number = input("Enter a credit card number #: ")
credit_number = credit_number.replace("-", "")
credit_number = credit_number.replace(" ", "")
credit_number = credit_number[::-1]
print(credit_number)

# step 2

for x in credit_number[::2]:
    sum_odd_digits += int(x)
    print(sum_odd_digits)
    
# step 3

for x in credit_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x
        
        
# step 4
total = sum_odd_digits + sum_even_digits
    
    
# step 5

if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")