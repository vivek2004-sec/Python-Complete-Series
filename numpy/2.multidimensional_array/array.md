# Arrays in Numpy:

A NumPy array (ndarray) is a collection of elements of the same data type stored in a multidimensional structure. Arrays provide an efficient way to store and perform operations on numerical data.

1.Number of dimensions in an array is called its rank.
-> ndim = number of dimensions

2.Size of the array along each dimension is called its shape.
-> Size of the array refers to total number of the elements it contains across all the dimensions.
-> ndarray.size
the total number of elements of the array. This is equal to the product of the elements of shape.

3.Elements are accessed using square brackets [] and arrays are commonly created from Python lists.
-> array = np.array([[1, 2, 3]])

4. In NumPy, shape tells you the size of an array along each of its dimensions.
   It's a tuple that describes the array's structure.
   For example : array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '$']]] )
   output : (3, 3, 3)
   -> (m, n, p)
   -> m : it means array has 3 layers.
   -> n : 3 rows
   -> p : each row has 3 columns.

5. Dimensions of array in python also called as axes.

6: Main objects:

# ndarray.ndim:

the number of axes (dimensions) of the array.
