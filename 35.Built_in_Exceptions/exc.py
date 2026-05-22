# Built in python Exceptions

# 1. BaseException:
# ->  This class is the root of Python's exception hierarchy. All other exceptions directly or indirectly inherit from it. 
# While it is rarely used directly in code, it is important because it forms the foundation of Python’s error-handling system.

try:
    raise BaseException("This is a BaseException")
except BaseException as e:
    print(e)
    
# 2. Exception:
# -> Exception class is the base for all non-exit exceptions. 
# You will often catch Exception in general error-handling code when you are not targeting a specific error type.

try:
    raise Exception("This is a generic exception")
except Exception as e:
    print(e)
    
# 3.  ArithmeticError:
# -> ArithmeticError class is the base for all errors related to mathematical operations. 
# You don’t usually raise it directly, but it provides a way to catch all math-related errors in one block.


try:
    raise ArithmeticError("Arithmetic error occurred")
except ArithmeticError as e:
    print(e)
    
    
# 4. ZeroDivisionError
# ZeroDivisionError occurs when you attempt to divide a number by zero. 
# Since division by zero is undefined in mathematics, Python raises this exception to signal the error.
    
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)
    
# 5. OverflowError
# OverflowError occurs when the result of a numerical operation is too large for Python to represent. 
# While it handles large integers well, certain floating-point operations (like very large exponentials) can still cause this error.

import math
try:
    result = math.exp(1000)  # Exponential function with a large argument
except OverflowError as e:
    print(e)
    
    
# 6. FloatingPointError
# FloatingPointError occurs when a floating-point calculation fails. By default, Python handles most floating-point issues silently (like dividing by zero results in inf or nan). 
 # However, you can explicitly enable floating-point error reporting with libraries like NumPy.
 
import numpy as np
np.seterr(all='raise')

try:
    np.divide(1, 0)
except FloatingPointError as e:
    print("FloatingPointError caught:", e)
    
# 7. AssertionError
# AssertionError is raised when the assert statement fails. The assert keyword is often used for debugging or testing assumptions in code.

try:
    assert 1 == 2, "Assertion failed"
except AssertionError as e:
    print(e)
    
# 8. AttributeError
# AttributeError occurs when you try to access or assign an attribute that does not exist for an object.

class MyClass:
    pass

obj = MyClass()

try:
    obj.some_attribute
except AttributeError as e:
    print(e)
    
    
# 9. IndexError
# IndexError happens when you try to access a list (or any sequence) element with an index that is out of range.

my_list = [1, 2, 3]

try:
    element = my_list[5]
except IndexError as e:
    print(e)
    
# 10. KeyError
# KeyError occurs when you try to access a dictionary key that doesn’t exist.

d = {"key1": "value1"}

try:
    val = d["key2"]
except KeyError as e:
    print(e)
    
# 11. MemoryError
# MemoryError occurs when Python cannot allocate enough memory for an operation. This usually happens when trying to create extremely large data structures.

try:
    li = [1] * (10**10)
except MemoryError as e:
    print(e)
    
# 12. NameError
# NameError occurs when you use a variable or function name that has not been defined.

try:
    print(vars)
except NameError as e:
    print(e)