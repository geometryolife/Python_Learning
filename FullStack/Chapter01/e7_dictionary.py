# 字典是另一种可变容器模型，而且可以存储任意类型的对象
# dic = {key1:value1, key2:value2}
# 列表是有序的对象，字典是无序的对象
# 字典的键必须使用不可变类型，如字符串、数字或元组，同一个字典键必须唯一
dic1 = {'A': '111', 'B': '222'}
print(dic1['A'], '\n')

# 创建字典
# 法1，先创建空字典，再赋值
dic1 = {}
dic1['name'] = 'joe'
dic1['age'] = 21
print(dic1)
# 法2, 直接创建字典并赋值
dic1 = {'name': 'joe', 'age': 21}
print(dic1, '\n')

# 访问字典中的值
dic1 = {'Name': 'joe', 'Age': 7, 'Class': 'First'}
print("dic1['Name']: ", dic1['Name'])
print("dic1['Age']: ", dic1['Age'])
print("dic1['Class']: ", dic1['Class'], '\n')

# 修改字典
dic1['Age'] = 18
dic1['School'] = "abc"
print("dic1['Age']: ", dic1['Age'])
print("dic1['School']: ", dic1['School'], '\n')

# 删除字典元素
dic1 = {'Name': 'joe', 'Age': 17, 'Class': 'First'}
# 删除字典的键
del dic1['Name']
print(dic1)
# 清空字典
dic1.clear()
print(dic1, '\n')
# 删除字典，dic1已经被删除，无法使用
del dic1
# print(dic1)

# 遍历字典
dic1 = {'name': 'joe', 'age': 20}
for idx, val in dic1.items():
    print("idx = {0}, val = {1}".format(idx, val))

for key in dic1.keys():
    print("key = {0}, val = {1}".format(key, dic1[key]))
print()

# 字典键的特性
# 字典的键必须唯一，若出现多次，只有最后一次出现的键值对生效
dic = {'Name': 'wangwu', 'Age': 17, 'Name': 'lisi'}
print("dic['Name']: ", dic['Name'], '\n')

# 字典的键必须不可变
dic1 = {('Name',): 'joe'}
# dic2 = {['Name', ]: 'joe'}


# >>> Execution Result:
# 111

# {'name': 'joe', 'age': 21}
# {'name': 'joe', 'age': 21}

# dic1['Name']:  joe
# dic1['Age']:  7
# dic1['Class']:  First

# dic1['Age']:  18
# dic1['School']:  abc

# {'Age': 17, 'Class': 'First'}
# {}

# idx = name, val = joe
# idx = age, val = 20
# key = name, val = joe
# key = age, val = 20

# dic['Name']:  lisi
