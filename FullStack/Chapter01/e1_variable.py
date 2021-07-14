a = 10
print(a)
# 变量类型
print(type(a))
# 内存地址
print(id(a), '\n')

a = 1.3
print(a, type(a))
print(id(a), '\n')

param1 = 3
param2 = 8
param3 = param1 + param2
print(param3)

# 同时为多个变量赋值
a = b = c = 1
print(a, b, c)
# 3个变量被分配到相同的内存空间上
print(id(a), id(b), id(c), '\n')

# 为多个对象指定多个变量
a, b, c = 1, 2, "Hello"
print(a, b, c)
# 3个变量被分配到相同的内存空间上
print(id(a), id(b), id(c))


# >>> Execution Result:
# 10
# <class 'int'>
# 9785184

# 1.3 <class 'float'>
# 139755138986096

# 11
# 1 1 1
# 9784896 9784896 9784896

# 1 2 Hello
# 9784896 9784928 139755139003504
