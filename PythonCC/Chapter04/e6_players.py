print("\n---------切片-----------")
#  切片--处理列表的部分元素
#  用法和range()函数类似，指定第一个元素和最后一个元素的索引
#  输出列表的前三个元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print("\n---------切片子集-----------")
#  提取列表的第2~4个元素，指定索引1~4
print(players[1:4])

#  如果未指定第一个索引，Python将从列表头开始
print(players[:4])

#  使用类似的语法，让切片终止于列表末尾
print(players[2:])

print("\n---------负数索引-----------")
#  输出名单上最后三名队员
print(players[-3:])

print("\n---------遍历切片-----------")
#  遍历前三名队员并打印他们的名字
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
