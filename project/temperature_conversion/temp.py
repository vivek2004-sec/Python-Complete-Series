print("******** Temperature Conversion ********")

print("F = Farenheit.")
print("C= Celsius.")
unit = input("Enter the unit to convert(F/C): ").capitalize()
temp = float(input("Enter the temperature: "))

if unit == "F":
    print("You are converting to Farenheit.")
    temp = (1.8 * temp) + 32.0
    print("Temperature is ", temp)
elif (unit == "C"):
    print("You are converting to Celsius.")
    temp = (temp - 32)/1.8
    print("The temperature is ", temp)
else:
    print("Invalide Input.")



print("****************************************")