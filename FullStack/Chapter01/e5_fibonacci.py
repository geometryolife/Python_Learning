# 用队列实现斐波那契数列
count = 10
a, b = 1, 1
ls = []

for i in range(count):
    ls.append(a)
    a, b = b, a + b

print(ls)


# >>> Execution Result:
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
