import numpy as np

# array = np.array('A') # 0
# print(array.ndim) # ndim = number of dimensions 


# array = np.array([1, 2])
# print(array.ndim)    # rank 1
# print(array.size)    # 2


# array = np.array([1, 2, 3, 4])
# print(array.ndim)             # rank 1

array = np.array([['A', 'B', 'C'], 
                  ['D', 'E', 'F'], 
                  ['G', 'H', 'I']])
print(array.ndim)                   # rank 2
print(array.shape)                  
print(array.size)                  


array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '$']]] ) 

print(array.ndim)                                                             # rank 3
print(array.shape)                                                            # (3, 3, 3)
print(array.size)
print(array[0][0][0])      # Chain indexing                                   # A
print(array[0, 0, 0])      # Multidimensional indexing                        # A
print(array[0, 0, 1])   
print(array[0, 0, 2])   
print(array[0, 1, 0])   
print(array[2, 2, 2])   
# print(array[layer-index, row-index, column-index])   

#  Create a word 'vivek'

print(array[2, 1, 0] + array[0, 2, 2 ] + array[2, 1, 0] + array[0, 1, 1]+ array[1, 0, 1])