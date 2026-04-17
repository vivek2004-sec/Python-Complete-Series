# Nested Loops:
# Python programming language allows to use one loop inside another loop which is called nested loop. 
# Following example illustrates the concept.

std = ['vivek', 'sujal', 'vijay', 'amey', 'saurabh', 'samarth', 'aditya']
v = len(std)
print(v)
nm = int(input("Enter the num: "))
while (nm == v):
    for i in std:
        print(i)
        
    break
