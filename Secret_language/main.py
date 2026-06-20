# Encoding & Decoding

import random
import string

def random_char() -> str:
    '''
    Generate a random string of 3 ASCII letters.
    
    >>> import random
    >>> random.seed(42)
    >>> random_chars
    'ZOX'
    '''
    return''.join(random.choices(string.ascii_letters, k=3))


print(string.ascii_letters)