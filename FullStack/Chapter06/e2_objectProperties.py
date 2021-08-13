import numpy as np

print("----------对象属性----------")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("数组各维的大小 = ", arr.shape)
print("数组的第一行的元素 = ", arr[0])
print("数组的第二行的元素 = ", arr[1])
print("数组的维数 = ", arr.ndim)
print("数组中元素的总数 = ", arr.size)
print("数组中元素的类型 = ", arr.dtype)
print("数组中每个元素占用的字节数 = ", arr.itemsize)


# >>> Execution Result:
# ----------对象属性----------
# 数组各维的大小 =  (2, 5)
# 数组的第一行的元素 =  [1 2 3 4 5]
# 数组的第二行的元素 =  [ 6  7  8  9 10]
# 数组的维数 =  2
# 数组中元素的总数 =  10
# 数组中元素的类型 =  int64
# 数组中每个元素占用的字节数 =  8
