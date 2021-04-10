#  将前10个整数的平方加入到一个列表中
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

print("--------------------")

#  为了代码更简洁，可不使用临时变量square
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

print("--------------------")

#  对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print("\n---------列表解析-----------")

#  列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value**2 for value in range(1, 11)]
print(squares)
