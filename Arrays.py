import numpy as np
import array
my_array = array.array('i')

arr1 = array.array('i', [1, 2, 3, 4])
print(arr1, my_array)
# np_array = np.array([], dtype=int)
# print(np_array)
# np_array1 = np.array([1, 2, 3, 4])
# print(np_array1)
# li = [1, 2, 3, 4]
# print(li)
arr1.insert(0, 6)
print(arr1)


def traverseArray(array):
    for i in array:
        print(i)


traverseArray(arr1)
print(arr1[-1])
