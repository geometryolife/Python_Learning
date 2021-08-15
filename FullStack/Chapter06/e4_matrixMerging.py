import numpy as np

print("----------矩阵合并----------")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# hstack()、vstack()参数要使用列表或元组传入
# 矩阵横向合并
print(np.hstack([arr1, arr2]), '\n')

# 矩阵纵向合并
print(np.vstack((arr1, arr2)))


"""
>>> Execution Result:
----------矩阵合并----------
[[1 2 5 6]
 [3 4 7 8]]

[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""
