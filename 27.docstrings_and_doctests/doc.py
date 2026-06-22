def add(a: int, b: int) -> int:
    """
    Adds two numbers.

    >>> add(2, 3)
    5
    >>> add(10, 20)
    30
    """
    return a + b
# The >>> lines are the inputs and the lines below them are the expected outputs.

print(add(2,3))



import random
import string


code = str(input("enter the code: "))
 
def random_char() -> str:
    """
    gives the set of random 3 ASCII charaters.
    
    >>> import random
    >>> random.seed(42)
    >>> random_char()
    'vox'
    
    """
    return"".join(random.choices(string.ascii_letters, k= 3))


def encode(code: str) -> str:
    """_summary_

    Args:
        code (str): _description_

    Returns:
        str: _description_
        
    -> Adds the 3 random characters to the code back $ forth.
    """
    
    
    if (len(code)) >= 3:
        code = code[1:] + code[0]
        code = random_char() + code + random_char()
    else:
        print(code)
    return code
    
    
print(encode(code))

print(random_char.__doc__)