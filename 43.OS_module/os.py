import os 

print(os.getcwd())
print(os.listdir())




# os.mkdir("new_folder")
# os.makedirs("folder1/folder2/folder3")

# os.remove("new.txt")

# os.rmdir("new_folder")
# os.removedirs("folder1/folder2/folder3")



# os.mkdir("new_folder")

# os.rename("new_folder", "vivek")

print(os.path.exists("vivek"))
print(os.path.isfile("vivek"))
print(os.path.isdir("vivek"))
print(os.path.getsize(".idea"))

print(os.name)
print(os.sep)



stats = os.stat("41.import/import.py")

print("Size:", stats.st_size, "bytes")
print("Last modified:", stats.st_mtime)
print("Permissions:", oct(stats.st_mode)[-3:])