# 内置函数
ls = list(range(1, 11, 1))
print("max = {0}, min = {1}".format(max(ls), min(ls)), '\n')


# 无参函数
def hello1():
    print("Hello World!")


hello1()
print()


# 有参函数
def hello2(name):
    print("Hello ", name)


hello2('joe')
print()


# 函数调用
def add(x, y):
    print("x={0}, y={1}".format(x, y))
    return x + y


a = add(1, 2)
b = add(y=2, x=3)
print(a, b, '\n')


# 函数也是特殊的对象
def summation(x, y):
    return x + y


add = summation
print(add(6, 1), '\n')


# 函数中的文档: 文档字符串
def addition(x, y):
    """
    这个函数实现加法运算，函数会返回一个加法运算的结果
    x: 输入(被加数)数字参数
    y: 输入(加数)数字参数
    """
    print("x = {0}, y = {1}".format(x, y))
    return x + y


print(addition(1, 1), '\n')
# print(help(addition))


# 默认参数
def printinfo(name, age=25):
    print("名字 = {0}, 年龄 = {1}".format(name, age))


printinfo(age=20, name='joe')
printinfo(name='joe')
print()


# 不定长参数
# 函数中用 *arg 方式接收数据，以元组(tuple)的形式传参
def func(x, *args):
    print("x = {0}, args = {1}".format(x, args))
    result = x
    for i in args:
        result = result + i
    return result


print("result = ", func(1, 2, 3))
# 可以不给 args 传参数
print(func(1), '\n')


# 函数中用 **kwargs 方式接收数据，以字典(dict)的形式传参
def func2(x, **kwargs):
    print("x = ", x)
    print("kwargs = ", kwargs)


print(func2(1, a=1, b=2, c=3))
print(type(func2), '\n')


# range() 函数
# range(start, stop[, step])
# range() 内只有一个参数时，默认从0开始生成数列
for i in range(5):
    print(i)
print()

for i in range(1, 5):
    print(i)
print()

for i in range(0, 30, 5):
    print(i)
print()

# range() 输出递减结果
for i in range(0, -5, -1):
    # 输出结果为从 0 ~ -5，步长为 - 1
    print(i)
print()

# 利用 range() 遍历字符串
x = 'abcde'
for i in range(len(x)):
    print(x[i])
print()

# range() 函数返回的结果是一个整数序列的对象，而不是列表，
# 但可以利用 list 函数返回列表
print(type(range(10)))
print(list(range(10)), '\n')


# 函数作为参数传递
def test(fun, a, b):
    """把 function 函数作为参数传递给 test 函数"""
    print(fun(a, b))


def function(x, y):
    return 2 * x + y


test(function, 1, 2)

# 解释: 函数可以作为一个对象进行参数传递。作为参数被传递的函数也称为回调函数。
# test() 函数的第一个参数 fun 就是一个函数对象。将函数 function() 作为参数传
# 递给 test() 函数，test 中的参数 fun 就拥有了函数 function() 的功能。因此可
# 以提高程序的灵活性。可以使用上面的 test() 函数，带入不同的函数参数。可以使
# 用 lambda 创建匿名函数作为函数参数，例如，使用 lambda 创建匿名函数实现
# z = 2 * x + y 方程式。
test((lambda x, y: 2 * x + y), 1, 2)
# test() 函数的第1个参数fun就是1个函数对象。将函数 function 传递给参数 fun，
# test 函数中的 fun() 就拥有了 函数 function 的功能。因此使用 lambda 创建匿
# 名函数可以提高程序的灵活性。可以用上面的 test 函数，带入不同的函数参数，
# 如使用 lambda 创建匿名函数实现 z = x² + y 方程式。
test((lambda x, y: x**2 + y), 1, 2)


# >>> Execution Result:
# max = 10, min = 1

# Hello World!

# Hello  joe

# x=1, y=2
# x=3, y=2
# 3 5

# 7

# x = 1, y = 1
# 2

# 名字 = joe, 年龄 = 20
# 名字 = joe, 年龄 = 25

# x = 1, args = (2, 3)
# result =  6
# x = 1, args = ()
# 1

# x =  1
# kwargs =  {'a': 1, 'b': 2, 'c': 3}
# None
# <class 'function'>

# 0
# 1
# 2
# 3
# 4

# 1
# 2
# 3
# 4

# 0
# 5
# 10
# 15
# 20
# 25

# 0
# -1
# -2
# -3
# -4

# a
# b
# c
# d
# e

# <class 'range'>
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4
# 4
# 3
