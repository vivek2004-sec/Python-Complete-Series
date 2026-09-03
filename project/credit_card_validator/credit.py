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