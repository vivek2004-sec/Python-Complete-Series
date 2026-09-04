# Banking Programm

def show_balance():
    print(f"The available balance is $ {balance:.2f} .")


def deposit():
    pass

def withdrawl():
    pass

balance  = 0
is_running = True

while is_running:
    print("Welcome to Bank")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()
    elif choice =="2":
        deposit()
    elif choice == "3":
        withdrawl()
    elif choice == "4":
        is_running = False
    else:
        print("This is not a valid Choice.")

print("You have a nice day.")