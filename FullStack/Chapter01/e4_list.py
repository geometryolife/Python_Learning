# Python 的列表可包含多种类型的元素
list1 = ['name', 'address', 2016, 2017]

# 字符串元素不可变，而列表元素可变
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a, '\n')

b = a[:]
print(a, b, '\n', sep='\n')

# 删除元素的两种方法
a[2:5] = []
del b[2:5]
print(a, b, '\n', sep='\n')

# 访问列表中的值，切片操作
list1 = [1, 2, 3, 4, 5, 6, 7]
print("lsit1[1]: ", list1[1])
print("list2[1:5]: ", list1[1:5], '\n')

# 列表翻转(反转)
ls = [1, 4, 5, 7, 11]
ls.reverse()
print(ls)
lang = list('hello')
print(lang[::-1], '\n')

# 更新列表
list1[1] = 10
print(list1)
list1.append(8)
print(list1, '\n')

# 删除元素
list1 = [1, 2, 3, 4, 5, 6, 7]
del list1[2]
print(list1)
# remove 方法删除列表中匹配的第一个值
list1.remove(1)
print(list1, '\n')

# 列表的组合与重复
print([5] + [6])
print([1] * 5, '\n')

# 列表的截取与拼接
list2 = ['a', 'b', 'c']
print(list2[2])
print(list2[-2])
print(list2[1:], '\n')

# 嵌套列表(可以构造多维列表)
a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
print(x)
print(x[0])
print(x[0][1], '\n')

# 列表排序
ls = [1, 4, 5, 7, 11]
# 升序
ls.sort()
print(ls)
# 降序
ls.sort(reverse=True)
print(ls, '\n')

# 列表转字典
ls = [('a', 1), ('b', 2)]
print(ls)
print(dict(ls))


# >>> Execution Result:
# [9, 2, 13, 14, 15, 6]

# [9, 2, 13, 14, 15, 6]
# [9, 2, 13, 14, 15, 6]


# [9, 2, 6]
# [9, 2, 6]


# lsit1[1]:  2
# list2[1:5]:  [2, 3, 4, 5]

# [11, 7, 5, 4, 1]
# ['o', 'l', 'l', 'e', 'h']

# [1, 10, 3, 4, 5, 6, 7]
# [1, 10, 3, 4, 5, 6, 7, 8]

# [1, 2, 4, 5, 6, 7]
# [2, 4, 5, 6, 7]

# [5, 6]
# [1, 1, 1, 1, 1]

# c
# b
# ['b', 'c']

# [['a', 'b', 'c'], [1, 2, 3]]
# ['a', 'b', 'c']
# b

# [1, 4, 5, 7, 11]
# [11, 7, 5, 4, 1]

# [('a', 1), ('b', 2)]
# {'a': 1, 'b': 2}
