countries = ("Spain", "Germany", "India", "U.S", "England")
temp = list(countries)
temp.append("Italy")
temp.reverse()
temp.insert(0, "Finland")
temp[2] = "Bharat"

print(temp)
temp.pop(5)
print(temp)



F1 = ("captain ameriaca", "iron man", "hulk")
F2 =("superman", "batman", "wondar woman")
F3 = F1 + F2
print(F3)

j = ( 1, 3, 4, 4, 4, 5, 6, 6 ,6 )
# print(j.count(4))
# print(j.count(6))
print(j.index(4, 2, 7))
# print(len(j))


# Reversing a Tuple

# Most common and Pythonic way to reverse a tuple is by using slicing with a step of -1, here is how we can do it:

num = (2, 3, 4, 5, 6, 7, 8)
print(num[::-1])


t = (1, 2, 3, 4, 5)  
# Reverse the tuple using the built-in reversed() function and convert it back to a tuple
rev = tuple(reversed(t))
print(rev)