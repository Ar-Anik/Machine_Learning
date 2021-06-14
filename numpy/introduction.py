import numpy
import time
import sys

a = numpy.array([1, 2, 3, 4, 5])
print("Numpy array : ", a)
print("first index : ", a[0])
print("last index : ", a[4])

# arr1 = numpy.array([1, 2, 3, 4])
# arr2 = numpy.array([5, 6, 7])
# print("Summation of two array : ", arr1 + arr2)
# This gives us error cz in numpy array operation array must be equal

arr1 = numpy.array([1, 2, 3])
arr2 = numpy.array([4, 5, 6])

print("Summation of two array :: ", arr1+arr2)
print("Subtraction of two array :: ", arr2-arr1)
print("Multiplication of two array :: ", arr1*arr2)
print("Division of two array :: ", arr2/arr1)

# Memory efficient checking
l = range(1000)
print("List Take : ", sys.getsizeof(8) * len(l))

array = numpy.arange(1000)
print("Numpy array Take : ", array.size * array.itemsize)

# Time efficient checking

size = 1000000

list1 = range(size)
list2 = range(size)

start = time.time()
result = [(x+y) for x,y in zip(list1, list2)]
end = time.time()
print("Python list take time : ", (end - start) * 1000)  # 1 sec = 1000 milisec

array1 = numpy.arange(size)
array2 = numpy.arange(size)

start = time.time()
result = array1 + array2
end = time.time()
print("Numpy array take time : ", (end - start) * 1000)
