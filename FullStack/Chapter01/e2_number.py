# Python3 有6个标准的数据类型(原生数据类型)
# 后四个为有序列的数据类型，序列中的每一个元素都会被分配序号。
# Number (数字) -> 整型、浮点型、复数
# Dictionary (字典)
# String (字符串)
# List (列表)
# Tuple (元组)
# Sets (集合)

# 复数
x = 123 - 12j
print(x.real)
print(x.imag, '\n')

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d), '\n')

# Python3 把 True 和 False 定义成关键字，它们的值为 1 和 0，可以和数字相加
x = True
y = x + 1
print(y, '\n')

# 加法
print(5 + 4)
# 减法
print(4.3 - 2)
# 乘法
print(3 * 7)
# 除法，得到一个浮点数
print(2 / 4)
# 除法，得到一个整数
print(2 // 4)
# 取余
print(17 % 3)
# 乘方
print(2 ** 5)


# >>> Execution Result:
# 123.0
# -12.0

# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

# 2

# 9
# 2.3
# 21
# 0.5
# 0
# 2
# 32
