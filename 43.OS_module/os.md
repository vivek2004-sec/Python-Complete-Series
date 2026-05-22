-> os module provides functions for interacting with operating system.
-> OS comes under python's standard utility module.
-> This module provides a portable way of using operating system-dependent functionality.

# OS Module in python:

1. OS stands for operating system.
2. It lets you talk to your computers operating system.
3. You can work with files, folders and systems using Python.
4. import os

# Functions:

1. getcwd: cwd -> current working dirctory.

2. Change Directory -> chdir()

3. Get files in directory -> listdir()

4. making new folder in current directory -> mkdir()

5. making multiple folders -> makedirs("folder1/folder2/folder3")
   -> Creates:

folder1/
└── folder2/
└── folder3/

6. removing a file -> os.remove("file name")

7. removing a folder -> os.rmdir("folder_name")

8. removing a multiple folders -> os.removedirs("folder1/folder2/folder3")

9. rename file or folder -> os.rename("new_folder", "vivek")

10. check a file or folder exists -> os.path.exists("folder_name")

11.check if it is file or folder -> os.path.isfile("folder_name") & os.path.isdir("folder_name")

12. Get file size -> os.path.getsize("folder_name")

13. Joining paths -> os.path.join("folder1", "folder2", "main.py")

14. get system information -> os.name / os.sep

15. run system commands -> os.system('cls') / system("dir")

16. Using os.stat(): os.stat() method is used to retrieve metadata about a file such as its size, permissions and timestamps.

st_size: Size in bytes
st_mtime: Last modified timestamp (UNIX time)
st_mode: File mode bits; we extract the last 3 digits for permission info
Similar to output of ls -l in Unix/Linux
