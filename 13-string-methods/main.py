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

# Strip & Replace:

s = "  hello  "

s.strip()        # "hello"    → removes both sides
s.lstrip()       # "hello  "  → removes left
s.rstrip()       # "  hello"  → removes right

"hello world".replace("world", "python")  # "hello python"
name = "vivek kamble"
new_name = name.replace("vivek", "rishi")
print(new_name) # rishi kamble

# Split & Join: 

"hello world".split()         # ["hello", "world"]
"a,b,c".split(",")            # ["a", "b", "c"]

" ".join(["hello", "world"])  # "hello world"
",".join(["a", "b", "c"])     # "a,b,c"

name = "vivek, kamble"
print(name.split(","))


# Check Type Content:
"hello".isalpha()    # True  → only letters
"123".isdigit()      # True  → only digits
"hello123".isalnum() # True  → letters and digits
"   ".isspace()      # True  → only whitespace
"Hello".istitle()    # True  → title case
"HELLO".isupper()    # True  → Upper case
"HELLO".islower()    # True  → Lower case