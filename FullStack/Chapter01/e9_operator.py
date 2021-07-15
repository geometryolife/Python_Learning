# 标识符:
# 以单下划线开头(_foo)代表不能直接访问的类属性，需要通过类提供的接口进行访问，
# 不能用 "from xxx import *" 导入。
# 以双下划线开头的(__foo)代表类的私有成员。j
# 以双下划线开头和结尾的(__foo__)代表特殊方法专用的标识，如 __init__() 代表
# 类的构造函数。

# Python 使用缩进来实现代码分组
# 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量

# 算术运算符: + - * / % ** //
# 比较运算符: == != > < >= <=
# 逻辑运算符: and or not
# 成员运算符: in 和 not in

a = 10
b = 20
list1 = [1, 2, 3, 4, 5]

if (a in list1):
    print("1 - 变量 a 在给定的列表 list1 中")
else:
    print("1 - 变量 a 不在给定的列表 list1 中")

if (b not in list1):
    print("2 - 变量 b 不在给定的列表 list1 中")
else:
    print("2 - 变量 b 在给定的列表 list1 中")

# 修改变量 a 的值
a = 2
if (a in list1):
    print("3 - 变量 a 在给定的列表 list1 中")
else:
    print("3 - 变量 a 不在给定的列表 list1 中", '\n')

# Python 中没有 switch-case 语句，而是使用 if-elif-else 语句


# >>> Execution Result:
# 1 - 变量 a 不在给定的列表 list1 中
# 2 - 变量 b 不在给定的列表 list1 中
# 3 - 变量 a 在给定的列表 list1 中
