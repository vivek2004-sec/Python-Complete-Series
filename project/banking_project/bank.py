# Banking Programm

def show_balance(balance):
    print(f"The available balance is $ {balance:.2f} .")


def deposit(balance):
    amount = float(input("Enter the amound to be deposited: "))
    print(f"The deposited amount is {amount:.2f} $. ")
    if amount < 0:
        print("Invalid amount.")
        return 0
    
    else:
        return amount 
    

def withdrawl(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient amount.")
        return 0        
    elif amount < 0:
        print("amoung must be greater than 0.")
        return 0
    else:
        return amount
    
    

    
        
def main():

    balance  = 0
    is_running = True

    while is_running:
        print("-----Welcome to Bank-----")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice =="2":
            balance += deposit()
        elif choice == "3":
            balance -= withdrawl(balance)
        elif choice == "4":
            is_running = False
        else:
            print("This is not a valid Choice.")
            print("---------------------------")

    print("You have a nice day.")
    
if __name__=='__main__':
    main()