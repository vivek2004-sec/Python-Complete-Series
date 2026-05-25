class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # ← private variable
                                    #   __ makes it private

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited → {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn → {amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance       # only way to access!

account = BankAccount(1000)
account.deposit(500)                # Deposited → 500
account.withdraw(200)               # Withdrawn → 200
print(account.get_balance())        # 1300

print(account.__balance)            # ❌ Error! private!