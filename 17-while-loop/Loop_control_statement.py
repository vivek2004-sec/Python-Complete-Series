# Loop control statements are used to change the normal flow of loops (like for and while). In Python, there are mainly 3 loop control statements:

# 🔹 1. break

for i in range(1, 6):
    if i == 3:
        break
    print(i)
   
   
# 🔹 2. continue

for i in range(1,6):
    if i == 3:
        continue
    print(i)
    
    
# 🔹 3. pass

for i in range(1, 6):
    if i == 3:
        pass
    print(i)
    
    
lt = (1, 2, 3, 4, 5, 6, 7, 8)
for num in lt:
    if num == 7:
        break
       
    print(num)
    
lt = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for num in lt:
    if  num == 7:
        continue
       
    print(num)
    
lt = (1, 2, 3, 4, 5, 6, 7, 8)
for num in lt:
    if  num == 7:
        pass
       
    print(num)
    


# | Statement  | Use                        |
# | ---------- | -------------------------- |
# | `break`    | Exit loop completely       |
# | `continue` | Skip current iteration     |
# | `pass`     | Do nothing                 |
# | `else`     | Runs if loop ends normally |
