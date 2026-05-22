<!-- In Python, the finally keyword is used in a try-except-finally block to define a section of code that will always execute, regardless of whether an exception occurs or not. It guarantees predictable code behavior, maintaining program stability even when errors arise. By using finally, developers ensure that cleanup operations and essential tasks are consistently performed, promoting code reliability and readability. -->

# Important Points -

-> finally block is always executed after leaving the try statement. In case if some exception was not handled by except block, it is re-raised after execution of finally block.
-> finally block is used to deallocate the system resources.
-> One can use finally just after try without using except block, but no exception is handled in that case.

# Syntax:

->
try:

# Code that may raise an exception

except ExceptionType:

# Code that handles the exception

finally:

# Code that always executes
