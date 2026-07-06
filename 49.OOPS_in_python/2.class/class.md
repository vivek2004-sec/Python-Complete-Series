Class :

A class is a collection of objects. Classes are blueprints for creating objects.
A class defines a set of attributes and methods that the created objects (instances) can have.

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator.

# class variables :

shared among all instances of class defined outside the constructor allow you to share all data among the objects
created from that class.
It's good to access the class variable by it's own class.

1782547657651_image.png
Jun 27
what is command line

Jun 30
Here's a clear explanation of Command Line:

What is Command Line?
A command line (also called CLI - Command Line Interface) is a text-based interface where you type commands to interact with your computer, instead of clicking buttons and icons like in a graphical interface (GUI).

GUI (Graphical) CLI (Command Line)
───────────────── ──────────────────
Click folder icon → type: cd folder
Click delete button → type: rm file.txt
Drag and drop file → type: mv file.txt destination
Different names for Command Line on different systems
Operating System What it's called
Windows Command Prompt (cmd) or PowerShell
Mac/Linux Terminal
Both Shell
Why use Command Line instead of GUI?
✅ Faster — one command does what 5 clicks would do
✅ More powerful — automate repeated tasks
✅ Essential for programming — run code, install packages
✅ Remote access — control servers without a screen
✅ Scripting — chain multiple commands together
Basic Command Line Commands (Windows PowerShell)
Command What it does
cd foldername Change directory (go into a folder)
cd .. Go back one folder
dir or ls List files in current folder
mkdir foldername Create a new folder
del filename Delete a file
cls Clear the screen
copy file1 file2 Copy a file
move file1 file2 Move/rename a file
python file.py Run a Python file
pip install package Install a Python package
Basic Command Line Commands (Linux/Mac Terminal)
Command What it does
cd foldername Change directory
ls List files
pwd Show current directory path
mkdir foldername Create folder
rm filename Delete file
clear Clear screen
cp file1 file2 Copy file
mv file1 file2 Move/rename file
cat filename Show file content
Your Daily Command Line Usage (from our conversation!)
You've already been using command line extensively:

bash
git clone https://github.com/... # download a repo
git add . # stage changes
git commit -m "message" # save changes
git push origin branch-name # upload changes
python script.py # run Python code
pip install package # install library
cd foldername # navigate folders
Command Line Prompt Structure
PS C:\Users\VIVEK\OneDrive\Desktop\New folder\python>
└──┬─┘ └──────────────┬──────────────────────────┘
│ │
"PS" means Current folder path
PowerShell you're working in
The > symbol means it's waiting for you to type a command.

In one line:

Command line is a text-based way to control your computer by typing commands instead of clicking — essential for programming, git, package management, and automating tasks.

You're already a command line user from all the git commands you've run! Want me to explain any specific command in more detail? 🚀

give me commands for windows so that i can copy and paste in notes

Jun 30
Here's the complete list of Windows commands to copy:

cd foldername - Change directory (enter a folder)
cd .. - Go back one folder
cd \ - Go to root directory (C:\)
dir - List files and folders
mkdir foldername - Create a new folder
rmdir foldername - Delete an empty folder
del filename - Delete a file
del /s foldername - Delete folder and all its contents
cls - Clear the screen
copy file1 file2 - Copy a file
move file1 file2 - Move or rename a file
ren oldname newname - Rename a file
type filename - Display file content
echo text - Print text to screen
exit - Close command prompt
where filename - Find location of a file
tree - Show folder structure as tree
attrib filename - View or change file attributes
find "text" filename - Search text inside a file
PowerShell specific commands:
Get-ChildItem - List files (same as dir/ls)
Set-Location foldername - Change directory (same as cd)
New-Item -ItemType Directory foldername - Create folder
Remove-Item filename - Delete file
Copy-Item file1 file2 - Copy file
Move-Item file1 file2 - Move file
Clear-Host - Clear screen
Get-Content filename - Display file content
Network commands:
ipconfig - Show network configuration
ping google.com - Test internet connection
nslookup google.com - DNS lookup
netstat - Show network connections
System commands:
systeminfo - Show system information
tasklist - Show running programs
taskkill /im name.exe - Stop a running program
shutdown /s - Shutdown computer
shutdown /r - Restart computer
Python related commands (your daily use):
python --version - Check Python version
python filename.py - Run a Python file
pip install packagename - Install a package
pip list - Show installed packages
pip uninstall packagename - Remove a package
python -m venv venv - Create virtual environment
venv\Scripts\activate - Activate virtual environment
Git commands (your daily use):
git clone url - Download a repository
git status - Check current changes
git add filename - Stage a file
git add . - Stage all files
git commit -m "message" - Save changes
git push origin branch - Upload changes
git pull origin branch - Download latest changes
git checkout -b branchname - Create new branch
git branch - List all branches
git log - Show commit history
Save this in your notes — these cover 90% of everyday command line usage! 🚀

```

CategoryInfo : WriteError: (C:\Users\VIVEK\...ming\45.file_IO:String) [Rename-Item], IOException
FullyQualifiedErrorId : RenameItemIOError,Microsoft.PowerShell.Commands.RenameItemCommand

PS C:\Users\VIVEK\OneDrive\Desktop\Python Programming> ren "45.file_IO" "45.file_io"
ren : Source and destination path must be different.
At line:1 char:1

ren "45.file_IO" "45.file_io"
```

CategoryInfo : WriteError: (C:\Users\VIVEK\...ming\45.file_IO:String) [Rename-Item], IOException
FullyQualifiedErrorId : RenameItemIOError,Microsoft.PowerShell.Commands.RenameItemCommand

PS C:\Users\VIVEK\OneDrive\Desktop\Python Programming>

Show more
Jun 30
This is a classic Windows issue — Windows treats filenames as case-insensitive, so renaming 45.file_IO to 45.file_io (just changing case) looks like "no change" to Windows and fails.

Fix — rename in 2 steps using a temporary name:

powershell
ren "45.file_IO" "temp_name"
ren "temp_name" "45.file_io"
This works because the temporary name is genuinely different, so Windows allows the first rename, then you rename it again to the proper lowercase version.

Alternative — using PowerShell's Rename-Item directly:

powershell
Rename-Item "45.file_IO" "45.file_io_temp"
Rename-Item "45.file_io_temp" "45.file_io"
Try the 2-step method above — it should work now! 🚀

class car:
def **int**(self, model, year, color, for_sale): # method
self.model = model
self.year = year
self.color = color
self.for_sale = for_sale

car1 = car("mustang", 2022, "black", False)
print(car1)
Jul 1
Your code has a bug — **int** should be **init**:

python
class Car:
def **init**(self, model, year, color, for_sale): # ✅ **init** not **int**
self.model = model
self.year = year
self.color = color
self.for_sale = for_sale

car1 = Car("Mustang", 2022, "Black", False)
print(car1.model) # Mustang
print(car1.year) # 2022
print(car1.color) # Black
print(car1.for_sale) # False
Two mistakes fixed:

1 — **int** → **init**
**init** is the constructor method that runs automatically when you create an object. **int** is something completely different — it converts an object to an integer.

2 — class car → class Car
Python convention says class names should always be CapitalCase (called PascalCase). Not required but strongly recommended.

Also — print(car1) prints the object memory address:

<**main**.Car object at 0x000001A2B3C4>
That's why you need print(car1.model) to see actual values.

To make print(car1) show useful info, add **str**:

python
def **str**(self):
return f"{self.year} {self.color} {self.model} - For Sale: {self.for_sale}"

print(car1) # 2022 Black Mustang - For Sale: False
Want me to explain classes and objects in more detail?

# what is (**init**)?

What is **init**?
**init** is a special method in Python that runs automatically when you create an object from a class.
It's called the constructor.

# What is self?

self refers to the current object being created. It's how the object refers to itself.
