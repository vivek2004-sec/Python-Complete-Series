# f = open("45.file_IO/mylife.txt", 'a')
# f.write("Hello this is vivek.")
# f.close()

# m = open("45.file_IO/vivek.txt", "w")
# m.write("Hello world!")
# m.close()

# f = open("requirements.txt", "r")
# text = f.read()
# print(text)
# f.close()

# Read Line by Line: 
f = open("45.file_IO/mylife.txt", "r")
line = f.readline()
print(line)
f.close()


# Read all lines as list: 
f = open("45.file_IO/mylife.txt", "r")
lines = f.readlines()
print(lines)
f.close()


# With statement: 

# with open("45.file_IO/mylife.txt", "w") as f:
#     f.write("Hello this is vivek.")
#     f.write("Hello this is rishi.")

with open("45.file_IO/mylife.txt", "r") as f:
    content = f.read()
    print(content)