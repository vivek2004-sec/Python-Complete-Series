

items = []
amount  = []
total = 0

while True:
    food = input("Enter the item you want to buy(q/quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("Enter the price: $"))
        items.append(food)
        amount.append(price)
        
    
    

print("____shopping Cart_____")
for food in items:
    print(food)

for i in amount:
    total += i
    
print(f"your total amount is {total}$")