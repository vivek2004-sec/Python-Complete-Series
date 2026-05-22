num = int(input("Enter the num: "))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")

else:
    print("Number is positive.")


marks = int(input("Enter the marks:"))
if marks >= 80:
    print("You got A grade.")
elif (50 < marks < 79):
    print("You have got B grade.")
elif(40 < marks < 50):
    print("You have got C grade.")
else:
    print("You are fail.")