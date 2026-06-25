"==" operator:

It is used for to check if two values are equal.
Use when comparing only values.
If the values are same it returns True.

"is" oparator:

Checks if two variables point to the same object in memory.
Use when checking if the variables point to same object in memory.
use in none.
returns False even if values are same but belongs to different objects in memory.

# Correct way to check None

if x is None:
...

# Not recommended

if x == None:
...
