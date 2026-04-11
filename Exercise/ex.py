import time
timestamp = time.strftime("%H:%M:%S", time.localtime())
print(timestamp)

hour = int(time.strftime("%H", time.localtime()))
if (hour < 12 ):
    print("Good morning!")
elif (12> hour > 4):
    print("Good afternoon!" )    
    
elif (4 > hour > 9):
    print("Good evening!")
    
else:
    print("Good night!")
    
    
    

# import time

# for i in range(2, 0, -1):  # Countdown from 10 to 1
#     print(i)
#     time.sleep(1)  # Wait 2 second between numbers

# print("Time's up! 🚀")

# print(range(5))  # Output: range(0, 5)
# print(list(range(5)))  # Output: [0, 1, 2, 3, 4]


# import time

# current_time = time.time()
# print("Current Timestamp:", current_time)


# import time

# start = time.time()  # Start time

# # Simulating a task
# for i in range(1000000):
#     pass  

# end = time.time()  # End time
# print("Execution Time:", end - start, "seconds")


# import time

# timestamp = time.time()  # Get the current timestamp
# readable_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
# print("Readable Time:", round(readable_time, 4), readable_time)


# import time

# input("Press Enter to start the stopwatch...")  
# start_time = time.time()  # Start time

# input("Press Enter to stop the stopwatch...")  
# end_time = time.time()  # End time

# elapsed_time = end_time - start_time  # Calculate the duration
# print("Elapsed Time:", round(elapsed_time, 3), "seconds")


import time
timestamp = time.strftime("%H:%M:%S", time.localtime())
print(timestamp)

hour = int(time.strftime("%H", time.localtime()))
if (hour < 12) :
    print("Good Morning!")
elif (12 > hour > 4 ) :
    print("Good Afternoon!")
elif (4 > hour > 8): 
    print("Good evening!")
else:
    print("Good Night!")