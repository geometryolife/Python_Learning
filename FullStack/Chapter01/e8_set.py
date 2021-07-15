# 集合的基本功能: 关系测试和删除重复元素
# 使用 {} 创建集合
# 注意: 要创建空集合必须使用 set() 函数，单独使用 {} 创建的是空字典

# 删除重复元素
basket = {'a', 'b', 'a', 'b', 'c', 'c'}
print(basket, '\n')

# 检测集合的成员
print('a' in basket)
print('d' in basket, '\n')


# 集合操作
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
# a - b: 在 a集合中，但不在 b 集合中
print(a - b)
# a | b: 在 a 集合 或 b 集合中的字母
print(a | b)
# a & b: 在 a 集合和 b 集合中都有的字母
print(a & b)
# a ^ b: a 集合和 b 集合中不同时存在的字母
print(a ^ b, '\n')


# >>> Execution Result:
# {'a', 'b', 'c'}

# True
# False

# {'d', 'r', 'b', 'a', 'c'}
# {'l', 'c', 'a', 'z', 'm'}
# {'b', 'r', 'd'}
# {'l', 'd', 'b', 'r', 'm', 'a', 'z', 'c'}
# {'c', 'a'}
# {'m', 'd', 'l', 'b', 'z', 'r'}
