import time

x = int(input("Enter the time: "))

for i in reversed(range(0, x+1)):
    print(i)
    time.sleep(1)
print("Time's Up!")