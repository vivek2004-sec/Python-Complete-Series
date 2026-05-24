# f = open("46.File_io_methods/myfile.txt", 'r')
# while True: 
#     line  = f.readline()
#     if not line:
#         break
#     print(line.strip())
# f.close()

# i = 0
# with open("46.File_io_methods/myfile.txt", 'r') as f:
#     while True:
#         i += 1

#         line = f.readline()
#         if not line:
#             break
#         m1 = line.split(",")[0]
#         m2 = line.split(",")[0]
#         m3 = line.split(",")[0]
#         print(f"Marks of student {i} in maths : {m1} ")
#         print(f"Marks of student {i} in maths : {m2} ")
#         print(f"Marks of student {i} in maths : {m3} ")
#         print(line.strip())


# with open("46.File_io_methods/myfile2.txt", "w") as f:
#     lines = ["Hello!\n", 'My name is vivek\n', "It's so nice to meet you."]
#     f.writelines(lines)
    
    
# Seek() function:
# seek()  → moves you to a SPECIFIC position in the file.

with open("46.File_io_methods/file.txt", "r") as f: 
    print(type(f))
    
    f.seek(10)
    
    data = f.read(5)
    print(data)
    
with open("46.File_io_methods/file.txt", "r") as f:
    f.seek(0)     # move to beginning
    f.seek(5)     # move to position 5
    f.seek(10)    # move to position 10