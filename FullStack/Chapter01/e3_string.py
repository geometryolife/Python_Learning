# 字符串
print(5 + 8)
print('5' + '8')

# 三引号(''')将字符串跨越多行
string = '''
11
22
333
444
'''
print(string)

# 连接字符串
print('a' * 3)
print('a' + 'b', '\n')

# 字符串格式化
# 格式字符串时，Python 使用一个字符串作为模版。模版中有格式符，这些
# 格式符为真实值预留位置，并说明真实数值应该呈现的格式。
# Python 用一个 tuple 将多个值传递给模版，每个值对应一个格式符。
# 模板和 tuple 之间，有一个 % 分隔，它代表了格式化操作。
print("name = %s, age = %d" % ('joe', 20), '\n')

# 取精度
print("digit = %.4f" % 10.12345, '\n')

# 原始字符串
print('a\nb')
print(r'a\nb', '\n')

# 转义字符(\)
print("let\'s go", '\n')

# 索引和切片
string = '0123456789'
print(string)
print(string[0])
print(string[-1])
print(string[0:-1])
print(string[2:5])
print(string[2:])
# 使用步长参数
print(string[0:5:2], '\n')

# 字符串翻转
lang = 'python'
print(lang[::-1], '\n')

# 基本操作
string = "hello"
print(len(string))
string = 'abcdef'
print('1' in string)
print('a' in string, '\n')

# 获取字符串中的最大值和最小值
str1 = 'abcd'
print(max(str1))
print(min(str1))

# 字符串格式化
# Python 支持格式化字符串的输出，使用 string.format() 的格式化方法，
# 其中{}作为占位符。
str1 = "my name is {} ".format('joe')
print(str1)
str2 = "my name is {0}, my age is {1}".format('tom', 21)
print(str2)


# >>> Execution Result:
# 13
# 58

# 11
# 22
# 333
# 444

# aaa
# ab

# name = joe, age = 20

# digit = 10.1235

# a
# b
# a\nb

# let's go

# 0123456789
# 0
# 9
# 012345678
# 234
# 23456789
# 024

# nohtyp

# 5
# False
# True

# d
# a
# my name is joe
# my name is tom, my age is 21
