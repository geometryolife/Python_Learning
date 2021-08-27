import numpy as np

print("----------矩阵的截取----------")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("\n----------按行列截取矩阵----------")
# 截取矩阵第0~1行的数据
# 截取阵型为二维矩阵的第1行数据
print(arr[0:1])
print(arr[0:1].shape, '\n')

# 截取矩阵第1行的数据(阵型为一维)
print(arr[0])
print(arr[0].shape, '\n')

# 截取矩阵第2行的数据(阵型为一维)
print(arr[1])
print(arr[1].shape, '\n')

# 截取矩阵第2行的3~5列的数据
print(arr[1, 2:5], '\n')

# 截取矩阵第2行中所有列的数据
print(arr[1, :], '\n')

# 截取矩阵前两列的数据
print(arr[:, 0:2], '\n')

print("\n----------按条件截取矩阵----------")
# 截取矩阵 arr 中大于6的元素，返回的是一维数组
# 对矩阵进行比较运算会生成一个布尔矩阵，将布尔矩阵传入 NumPy 数
# 组的方括号 [] 实现截取。
arr2 = arr[arr > 6]
print(arr2, '\n')

# 打印 arr 矩阵大于6的元素生成的布尔矩阵
print(arr > 6, '\n')

# 按条件截取数组，使用较多的是对矩阵中满足一定条件的元素变成特定
# 的值。例如，将矩阵中大于6的元素变成0
arr[arr > 6] = 0
print(arr, '\n')

print("\n----------遍历矩阵----------")
# 遍历矩阵中大于6的元素，并将元素的值设置为0，可以使用循环来遍历矩阵
data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
rowNum = data.shape[0]
colNum = data.shape[1]
print(rowNum)
print(colNum)

# 遍历设置矩阵元素的值
for x in range(rowNum):
    for y in range(colNum):
        if data[x, y] > 6:
            data[x, y] = 0
print(data)


"""
>>> Execution Result:
----------矩阵的截取----------

----------按行列截取矩阵----------
[[1 2 3 4 5]]
(1, 5)

[1 2 3 4 5]
(5,)

[ 6  7  8  9 10]
(5,)

[ 8  9 10]

[ 6  7  8  9 10]

[[1 2]
 [6 7]]


----------按条件截取矩阵----------
[ 7  8  9 10]

[[False False False False False]
 [False  True  True  True  True]]

[[1 2 3 4 5]
 [6 0 0 0 0]]


----------遍历矩阵----------
2
5
[[1 2 3 4 5]
 [6 0 0 0 0]]
"""
