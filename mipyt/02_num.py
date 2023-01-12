import numpy as np
# create a NumPy array, the first of many. Like matlab matrixes!
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array) # prettyprint
print(array.shape) # like matlab size(array)
print(array.dtype)
print('')

# but unlike matlab we can nest deeper than R^2
cube = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"cube has dimensions: {cube.ndim}") # number of dimensions (3 in this case)

arry2 = (array - 1)/2
print(arry2)
print(arry2.dtype) # automatically retyped
print('')

print(array > 5)
print('')

(array > 3) & (array < 8) # and or not cannot be used, bitwise are used with np arrays.
# remember to always use () because of confusing operator precedence

# operations between two arrays are elementwise by default, yes!! Like matlab .*
array+arry2
array * [[2, 2, 2], [10, 10, 10], [5, 4, 3]] # np.array * regular list will convert the list to np.array :)

array[1][2] # standard select works, like with an ordinary nested list
array[:, 2] # BUT RATHER USE MATRIX SELECT - it's faster and cleaner!
array[0:-1, 1:] # it does stuff..
array[array > 5] # select via a matrix of booleans, but only as a vector, position is lost :(
array * (array > 5) # this is the way to pick only elements > 5 (others are zero)
array[[0, 2, 2, 1], :] # select via array of indices, and it can even be duplicated
array[(0, 2, 2, 1), :] # tuple works just the same

# broadcasting
array * [0, 1, 10] # columnwise multiplication with a row vector
array * [[0], [1], [10]] # rowwise multiplication with a col vector
# array * [[0], [1]] # error of course

arry2[0, 0] = -1 # normal assignment as expected
arry2[:, 1] = 0 # broadcasting assignment (set whole column to constant)
arry2[:, 1] = [3, 5, 7] # set column to values (note: assign row vector, even though we are assigning col)
# generally speaking, any syntax that selects can be used for assignment

arry2 *= 2 # oh and these things of course work too :)
arry2 = arry2 * 2 # looks same, but this is NOT THE SAME
# += mutates the matrix, while = creates new matrix!

# mutation may be preferred, but there are gotchas
try:
    array /= 2 # cannot mutate matrix when it would change type (from int to float)
    array = array / 2 # this is correct in this case
except Exception as e:
    print('Chyba!!', type(e))


# MATRIX GENERATION FUNCTIONS
np.zeros((4, 4))
np.ones((4, 4))
np.ones((4, 4), dtype='float64') # specifies type explicitly instead of using inferred
np.zeros(4, dtype=bool)
np.full((4, 4), 7.34) # equivalent to np.ones((4, 4)) * 7.34
np.eye(4)
np.diag([1, 2, 3, 4, 5])
np.arange(100, 140, 3) # like python range, it creates a vector (min, max, step)
np.arange(0.0, 50.0, 0.3)[-1] # NOPE!! Beware that arange accumulates floating point error! -> DO NOT USE ARANGE FOR FLOATS
np.linspace(3, 31.76, num=11) # this is good for floats (start & end values are exact)
np.random.random((4, 2)) # 4x2 random values 0 to 1

arr = np.arange(12)
reshaped = arr.reshape(3,4) # this should be a new matrix, it has different shape after all?
reshaped[2, 2] = 99 # arr should not be mutated by this
arr # but IT IS, the reshape is just a different view of the same matrix and it's byRef. Whaaat?

sub_arr = arr[2:4]
sub_arr[:] = 77
arr # again, arr is mutated because the sliced subarray is just a byRef view of original arr

arr.reshape((3, 4)).copy() # this creates a truly new matrix

transposed = arr.reshape(3,4).T # transposition; same as above applies
# when working with NumPy programs, always check whether a function mutates, creates a view or a new matrix!

# since python 3.5 there is an operator for matrix multiplication, but normal python data types do not work with it
# NumPy matrices implement it :)
array1 = np.array([[1, 2, 3], [4, 5, 6]]) # 2x3
array2 = np.array([[1, 0, 0, 7], [0, 2, 0, 1], [0, 0, 3, 0]]) # 3x4
array1 @ array2 # 2x4
# otherwise we can use function np.dot but @ is better

# if np.eye(3): # NOPE, the truth value of array with more than one elem is ambiguous, but we can do these:
if np.eye(3).any():
    print('at least one element in eye(3) is non-zero')
if np.eye(3).all():
    print('all elements in eye(3) are non-zero')
if np.zeros((4, 4)).size:
    print('zeros((4,4)) is not empty')

# btw do not use math, use the functions and constants from np
x = np.linspace(0, 2*np.pi, num=1000)
sinx = np.sin(x) # because it supports vector input
