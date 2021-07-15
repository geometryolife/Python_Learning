# 计算 1 ~ 10 的总和
n = 10
summation = 0
counter = 1
while counter <= n:
    summation = summation + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, summation))

# 在 while 循环中使用 else 语句，在 while-else 条件语句为 False 时
# 执行else 的语句块，此时 else 有延续变量作用域的作用。
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")
print()

# for 语句
languages = ['C', 'C++', 'Perl', 'Python']
for x in languages:
    print(x, end=' ')
print('\n')

# 使用 range() 函数生成一系列数
for i in range(5, 9):
    print(i, end=' ')
print('\n')

# 对 10 以内的数求和
summation = 0
for i in range(1, 10):
    summation = summation + i

print("summation = %d" % summation, '\n')

# 结合 range() 和 len() 函数以遍历一个序列的索引
data = ['a', 'b', 'c', 'd']

for i in range(len(data)):
    # print('index = ', i, ', data = ', data[i])
    print("index = {}, data = {}".format(i, data[i]))
print()

# break 语句，结束当前循环块中的剩余语句
for letter in 'abcd':
    print("当前字母为: ", letter)
    if letter == 'c':
        break
print()

# continue 语句，跳过当前循环块中的剩余语句，然后继续进行下一轮循环
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print("i = ", i)
print()

# 使用枚举遍历序列
# 使用枚举的同时得到序列的元素和元素值
sequence = [10, 20, 30]
for index, item in enumerate(sequence):
    print("index = {}, data = {}".format(index, item))


# >>> Execution Result:
# 1 到 10 之和为: 55
# 0  小于 5
# 1  小于 5
# 2  小于 5
# 3  小于 5
# 4  小于 5
# 5  大于或等于 5

# C C++ Perl Python

# 5 6 7 8

# summation = 45

# index = 0, data = a
# index = 1, data = b
# index = 2, data = c
# index = 3, data = d

# 当前字母为:  a
# 当前字母为:  b
# 当前字母为:  c

# i =  1
# i =  3
# i =  5
# i =  7
# i =  9

# index = 0, data = 10
# index = 1, data = 20
# index = 2, data = 30
