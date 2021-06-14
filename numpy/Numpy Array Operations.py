import numpy

# 1 Dimensional Array
a = numpy.array([1, 2, 3, 4, 5, 6])
print(a)

# 2 Dimensional Array
b = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)

# Array Dimension
print("Array Dimension :: ", a.ndim)
print("Array Dimension :: ", b.ndim)

# Array element Size
print("a Array Each Element Size :: ", a.itemsize)
print("b Array Each Element Size :: ", b.itemsize)

# Data Type
print("a Array Element Data Type :: ", a.dtype)
print("b Array Element Data Type :: ", b.dtype)

# Data Type Change of array
c = numpy.array([1, 2, 3, 4, 5], dtype = numpy.float64)    # convert integer to float
d = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype = numpy.float64)   # convert integer to float

print("c Array :: \n", c)
print("d Array :: \n", d)

print("c Array Element Data Type :: ", c.dtype)
print("d Array Element Data Type :: ", d.dtype)

c = numpy.array([1, 2, 3], dtype = complex)    # convert integer to complex number
d = numpy.array([[1, 2], [3, 4], [5, 6]], dtype = complex)  # convert integer to complex number

print("c Array :: \n", c)
print("d Array :: \n", d)

print("c Array Element Data Type :: ", c.dtype)
print("d Array Element Data Type :: ", d.dtype)


# Size of array
a = numpy.array([[1, 2], [3, 4], [5, 6]])
print("Size of Array :: ", a.size)

# Array shape means row and column
print("Row and Column of Array a :: ", a.shape)

#

