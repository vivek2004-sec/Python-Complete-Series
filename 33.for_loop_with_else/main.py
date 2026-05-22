i = 0
while i < 7:
    print(i)
    i += 1 
else:
    print("Sorry no i")

for x in range (5):
    print("Iteration no {} in for loop".format(x + 1))

else:
    print("else block in loop")
print("Out of loop")


num = int(input("enter the number:"))
while num > 1:
    print("you are free to go.")
    break

else:
    print('sorry')
    
    
ls = ["mango", "apple", "oranges", "grapes"]
for fruits in ls:
    print(fruits)

else:
    print("the apple.")