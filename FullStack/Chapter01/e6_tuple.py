# 创建元组
tup1 = ('a', 'b', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tup4 = 1, 2, 3
tup5 = 1,
print(tup1, tup2, tup3, tup4, tup5, '\n', sep='\n')

# 使用元组给多个变量赋值
tup1 = 1, 2, 3
x, y, z = tup1
print(tup1)
print("x={0}, y={1}, z={2}".format(x, y, z), '\n')

# 创建空元组
tup1 = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
tup1 = (50)
print(type(tup1))
tup1 = (50,)
print(type(tup1), '\n')

tup1 = ('a', 'b', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5], '\n')

# 元组反转
print(tup1[::-1])

# 元组无法修改元素值，但可以修改元组
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3, '\n')

# 删除元组
tup = ('jd', 'taobao', 1997, 2000)
print(tup, '\n')
del tup
# print(tup)

# 连接与组合
print((1, 2, 3) + (4, 5, 6))
print(('a',) * 3, '\n')

# 元组索引与截取
tup = ('a', 'b', 'c')
print(tup[2])
print(tup[-2])
print(tup[1:])


# >>> Execution Result:
# ('a', 'b', 1997, 2000)
# (1, 2, 3, 4, 5)
# ('a', 'b', 'c', 'd')
# (1, 2, 3)
# (1,)


# (1, 2, 3)
# x=1, y=2, z=3

# <class 'int'>
# <class 'tuple'>

# tup1[0]:  a
# tup2[1:5]:  (2, 3, 4, 5)

# (2000, 1997, 'b', 'a')
# (12, 34.56, 'abc', 'xyz')

# ('jd', 'taobao', 1997, 2000)

# (1, 2, 3, 4, 5, 6)
# ('a', 'a', 'a')

# c
# b
# ('b', 'c')
