import time

x = int(input("Enter the time: "))

for i in range( x, 0, -1):
    print(i)
    time.sleep(1)
print("Time's Up!")