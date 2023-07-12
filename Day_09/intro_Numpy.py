import numpy as np

arr = np.array([1, 3, 4, 5, 9])
arr1 = np.array((0, 3, 4, 5, 9))
print(arr, type(arr), arr1)
print(np.__version__)

# Dimensions
zeroDimensionArr = np.array(50) # 0 dimension
# print(zeroDimensionArr)

oneDimensionArr = np.array([1, 5, 7]) # 0 dimension
# print(oneDimensionArr)

twoDimensionArr = np.array([[1, 5, 7], [2, 3, 1], [1, 4, 'a'], [1, 4, 'a']]) # 0 dimension
# print(twoDimensionArr)

threeDimensionArr = np.array([[[[[[[1, 5, 7], [2, 7, 9], [2, 3, 1]]]]]]]) # 0 dimension
# print(threeDimensionArr)
# Check number of dimensions
# print(zeroDimensionArr.ndim)
# print(oneDimensionArr.ndim)
# print(twoDimensionArr.ndim)
# print(threeDimensionArr.ndim)

arr2 = np.array([1, 2, 3, 4], ndmin=5)
# print(arr2, arr2.ndim)

# Indexing
# print(oneDimensionArr[0] + oneDimensionArr[1])
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)
print(arr3[0, 1, 1])
