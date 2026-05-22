Python exception handling lets you gracefully handles unexpected events (like invalid inputs or missing files) without crashing.
Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.

Keywords used:

try:
-> contains the code that might fail.

except:
-> Runs if specific error occurs in the 'try' block.

# Difference between Errors and Exceptions

both are issues in the code but both differ very sevarily.

Errors : These are the issues in the program logic, syntax errors etc. occurs at compile time.
Exceptions : these are the issues occured at the runtime and can be handled by the exception handling.(e.g. invalid inputs, missing files)

# Syntax of Exception Handling:

try: # Code
except SomeException: # Code
else: # Code
finally: # Code

1.try: Runs the risky code that might cause an error.
2.except: Catches and handles the error if one occurs.
3.else: Executes only if no exception occurs in try.
4.finally: Runs regardless of what happens useful for cleanup tasks like closing files.
