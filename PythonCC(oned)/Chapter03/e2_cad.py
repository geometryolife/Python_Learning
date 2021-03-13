#  修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

print("--------------------")

#  在列表中添加元素
#  1.追加: 在列表末尾添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print("--------------------")

#  利用append()方法动态创建列表，创建空列表，再使用一些列append()语句添加元素
motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

print("--------------------")

#  2.在列表中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

print("--------------------")

#  从列表中删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#  1.使用del语句删除元素(知道要删除的元素在列表中的位置)
#  del语句删除的值，将无法再访问
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

print("--------------------")

#  2.使用pop()方法删除元素，可接着使用被弹出的值
#  列表就像一个栈，删除列表末尾的元素相当于弹出栈顶端的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print("--------------------")

#  假设列表中的摩托车时按购买时间存储的，就可以使用方法pop()打印一条消息，
#  指出最后购买的是哪款摩托车:
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

print("--------------------")

#  3.弹出列表中任何位置处的元素
#  指定pop()的参数: 即在括号中指定要删除的元素的索引
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#  经验: 如果要从列表中删除一个元素，且不再使用它，那么用del语句
#  如果在删除元素后，还想继续使用它，就使用pop()方法

print("--------------------")

#  4.根据值删除元素
#  不知要删除的值所处的位置，想删除元素的值，可用方法remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print("--------------------")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#  注意: 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，
#  就需要使用循环来判断是否删除了所有这样的值。
