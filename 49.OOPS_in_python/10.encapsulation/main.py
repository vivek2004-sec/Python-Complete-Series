class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  #private variable
        
        
    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            
            
    def withdrawl(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            
        else:
            print("IN-valid amount")
            
    def get_balance(self):
        return self.__balance



acc1 = Bankaccount("Pappu", 10000)
acc1.__balance = 100000
print(acc1.__balance)
acc1.deposit(5000)
print("1st", acc1.name, acc1.get_balance())
acc1.withdrawl(2000)
print("2nd", acc1.name, acc1.get_balance())


class TestScores:
    def __init__(self, sub1, sub2, sub3, total):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.__total = total
        
    def add_marks(self, marks):
        if 0<= marks <= 100:
            self.__total += marks
            
        
    def get_marks(self):
        return self.__total
        
        

    
        
        

yash = TestScores('maths', 'science', 'history', 180)
yash.__total = 250
yash.add_marks(30)

print(yash.get_marks())