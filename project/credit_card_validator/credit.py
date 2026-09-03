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
    # if x > 10:
        
    