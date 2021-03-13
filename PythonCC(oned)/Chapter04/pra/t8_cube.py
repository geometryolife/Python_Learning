#  将同一个数字乘三次称为立方。请创建一个列表，其中包含前10个整数(即1~10)
#  的立方，再使用一个for循环将这些立方数都打印出来
cubes = []

for number in range(1, 11):
    cubes.append(number ** 3)

print(cubes)

#  for循环打印
for cube in cubes:
    print(cube)
