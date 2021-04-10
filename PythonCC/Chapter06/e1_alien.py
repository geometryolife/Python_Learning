print("----------简单的字典----------")
#  字典能够高效地模拟现实世界中的情形
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print("\n----------使用字典----------")
#  字典用放在花括号{}中的一系列键-值对表示，键、值之间用冒号分隔
#  字典中，可存任意多个键-值对，最简单的字典只有一个键-值对
alien_0 = {'color': 'green'}
print(alien_0)

#  访问字典中的值
print(alien_0['color'])

print("\n----------访问字典中的值----------")
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")

print("\n----------添加键-值对----------")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#  注意: Python不关心键-值对的添加顺序，只关心键和值之间的关联关系。(无序)

print("\n----------先创建一个空字典----------")
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print("\n----------修改字典中的值----------")
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

print("\n----------外星人右移例子----------")
#  对一个能够以不同速度移动的外星人的位置进行跟踪
#  存储外星人的当前速度，并据此确定该外星人将向右移动多远
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

#  向右移动外星人
#  据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #  这个外星人的速度一定很快
    x_increment = 3

#  新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#  修改外星人字典中的值，可改变外星人的行为
alien_0['speed'] = 'fast'
print(alien_0)

print("\n----------删除键-值对----------")
#  del语句: 指定字典名和要删除的键
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#  删除的键值对永远消失了
del alien_0['points']
print(alien_0)
