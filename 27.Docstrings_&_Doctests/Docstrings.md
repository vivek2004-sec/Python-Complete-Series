# Docstrings

Python Docstrings are the strings literals that appear right after the definition of a functions, methods, class, or modules.
used to document our code.
This are used to describe any function. so that other's also could understand our program.
But Docstrings are also used for testing purposes.

# Doctest

A doctest is a way to test your code inside docstring itself.You write an example of how the function works, and Python runs it automatically to check if the output is correct.

# Why use doctests?

1. Proves your function actually works
2. Doubles as documentation — shows real examples
3. Required by many open source projects like TheAlgorithms
4. CI systems run them automatically on every PR

To run doctest do this:

python -m filename.py -v
