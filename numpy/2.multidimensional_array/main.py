import numpy as np

# array = np.array('A') # 0
# print(array.ndim) # ndim = number of dimensions 


# array = np.array([1, 2])
# print(array.ndim)         # rank 1


# array = np.array([1, 2, 3, 4])
# print(array.ndim)             # rank 1

array = np.array([['A', 'B', 'C'], 
                  ['D', 'E', 'F'], 
                  ['G', 'H', 'I']])
print(array.ndim)                   # rank 2
print(array.shape)                  


array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '$']]] ) 

print(array.ndim)                                                             # rank 3
print(array.shape)                                                            # (3, 3, 3)
print(array[0][0][0])                                                         # A