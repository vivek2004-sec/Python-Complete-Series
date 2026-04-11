# Break statement: It enables a program to skip over a part of the code.A break statement terminates the very loop it lies within.
# exits loop.
# for i in range(9):
#     print("5 X", i+1, "=", 5 * (i+1))
#     if (i == 5):
#      break
 
# print("Done with the loop.")
    
# for i in range(9):
#     if (i == 5):
#      break
#     print("5 X", i+1, "=", 5 * (i+1))
# print("Done with the loop.")

# continue: exits the iteration
# skips the rest of the code in the loop and moves to the next iteration.   

for i in range(10):
    if (i == 6):
     print("Skip the iteration.")
     continue
    print("5 X", i, "=", 5 * (i))
print("Done with the loop.")