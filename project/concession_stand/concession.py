menu = {
    "Pizza": 3.00,
    "Nachos": 2.19,
    "Popcorn": 6.00,
    "Fries": 2.50,
    "Pretzel": 3.19,
    "Soda": 2.34,
    "Lemonade": 4.25
}

cart = []
total = 0

print("-------Menu-------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------------------")


while True:
    food = input("Select an item from the menu(q to quit): ").title()
    if ( food == "Q"):
        break
    elif menu.get(food) is not None:
    
        cart.append(food)

print(cart)
        