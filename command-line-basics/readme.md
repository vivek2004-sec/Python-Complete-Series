# What is Command Line?

A command line (also called CLI - Command Line Interface) is a text-based interface where you type commands to interact with your computer, instead of clicking buttons and icons like in a graphical interface (GUI).

# Why use it?

✅ Faster — one command does what 5 clicks would do
✅ More powerful — automate repeated tasks
✅ Essential for programming — run code, install packages
✅ Remote access — control servers without a screen
✅ Scripting — chain multiple commands together

# Windows commands:

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

# PowerShell specific commands:

Get-ChildItem - List files (same as dir/ls)
Set-Location foldername - Change directory (same as cd)
New-Item -ItemType Directory foldername - Create folder
Remove-Item filename - Delete file
Copy-Item file1 file2 - Copy file
Move-Item file1 file2 - Move file
Clear-Host - Clear screen
Get-Content filename - Display file content
