# Match case statement:
# match-case statement is Python's version of a switch-case found in other languages.
# It allows us to match a variable's value against a set of patterns.


x = int(input("Enter the value of x:"))
# x is the variable to match.

match x:    
    # if x is 0.
    case 0:
        
        print("x is zero.")
        # case with if - condition.
    case 6 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    case _ if x < 10: 
        print("x is < 10.")

        
    case _ if x != 80:
        print(x, "x is not 80")
        
    case _ if x >= 60:
        print(x, " x is greater than 60.")
        
