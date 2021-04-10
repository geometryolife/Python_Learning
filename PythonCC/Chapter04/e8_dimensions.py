print("---------元组-----------")
#  定义元组，不可变
#  类似于列表，元组使用圆(小)括号而非方(中)括号
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#  尝试修改元组dimensions中的一个元素，操作禁止
#  不能修改元组的元素
#  dimensions[0] = 250

print("\n---------遍历-----------")
for dimension in dimensions:
    print(dimension)

print("\n---------修改元组变量-----------")
#  虽然不能修改元组的元素，但可以给存储元组的变量赋值
#  如果要修改前述矩阵的尺寸，可重新定义整个元组
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#  相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周
#  期都不变，可使用元组。
