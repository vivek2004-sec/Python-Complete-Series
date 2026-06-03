# Case Methods:

s = "hello world"

s.upper()        # "HELLO WORLD"
s.lower()        # "hello world"
s.capitalize()   # "Hello world"
s.title()        # "Hello World"
s.swapcase()     # "HELLO WORLD" → swaps upper/lower


# Search & Check:

s = "hello world"

s.find("world")      # 6  → returns index, -1 if not found
s.index("world")     # 6  → same but raises ValueError if not found
s.count("l")         # 3
s.startswith("hello") # True
s.endswith("world")   # True
"world" in s          # True
