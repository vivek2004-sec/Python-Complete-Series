tup = (1,5, 7, "green", True)
print(type(tup), tup)

print(tup[1])
print(tup[0:3])
print(tup[1:4])
print(tup[:-2])

n = int(input("Enter the number:"))
if n  in tup:
    print(n," is present in tup.")
else:
    print(n," is not present in tup.")
