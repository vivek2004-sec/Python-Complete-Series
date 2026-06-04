import time

for i in range(2, 0, -1):  # Countdown from 10 to 1
    print(i)
    time.sleep(1)  # Wait 2 second between numbers

print("Time's up!")

import time

for i in range(5,-1, -1):
    print(i)
    time.sleep(1)
print("Time's up! ")

name = {"vivek": 22, "sujal": 21, "amey": 21}
for key, value in name.items():
    print(key,"=", value)