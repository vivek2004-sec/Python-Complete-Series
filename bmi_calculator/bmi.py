print("********* BMI CALCULATOR *********")

weight = int(input("Enter the weight: "))

height = int(input("Enter the height: "))

height /= 100
height = height**2

bmi = weight/height

print("The BMI is ", round(bmi))

print("**********************************")

