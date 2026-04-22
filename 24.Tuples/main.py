tup = (1,5, 7, "green", True)
print(type(tup), tup)

print(tup[1])
print(tup[0:3])
print(tup[1:4])
print(tup[:-2])
print(tup[0:4])
print(tup[:-4])
print(tup[:-2])

n = int(input("Enter the number:"))
if n  in tup:
    print(n," is present in tup.")
else:
    print(n," is not present in tup.")

a = (1, 2, 3, 4, [1, 2, 3, 4, 5], {'vivek':1, 'sujal': 3}, 'vivek', 'usual')
print(a)


tup1 = (2, 3, 4, 5)
tup2 = ('vivek', 'kamble')
tup3 = tup1 + tup2
print(tup3)