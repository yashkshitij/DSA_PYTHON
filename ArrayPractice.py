from array import *

arr = array('i', [1, 2, 3, 4, 5])
print(arr)

for i in arr:
    print(i)

print(arr[0])


arr.append(6)
print(arr)

arr.insert(3, 78)
print(arr)

arr1 = array('i', [0, 9, 8, 7, 6, 5])
arr.extend(arr1)
print(arr)
arr.remove(1)
print(arr)

li = [21, 22, 34]
arr.fromlist(li)
print(arr)
arr.pop()
print(arr)
print(arr.index(6))

# arr.reverse()
# print(arr)
# arr.reverse()
print(arr.buffer_info())
print(arr.count(21))
# arr.tostring()
# print(arr)
# print(`arr+' '`)

# print(arr.tolist())
print(arr[1:2])
