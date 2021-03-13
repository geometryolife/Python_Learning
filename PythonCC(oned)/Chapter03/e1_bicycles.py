#  列表: 由一系列特定顺序排列的元素组成
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print("--------------------")

#  访问列表元素
print(bicycles[0])
print(bicycles[0].title())

print("--------------------")

#  索引从0而不是从1开始
#  访问第2、4个元素
print(bicycles[1])
print(bicycles[3])

print("--------------------")

#  使用负数索引
print(bicycles[-1])

print("--------------------")

#  使用列表中的各个值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
