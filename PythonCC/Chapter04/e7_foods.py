print("---------复制列表-----------")
#  同时省略起始索引和终止索引
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n---------验证-----------")

#  为核实我们确实有两个列表，在每个列表中都添加一种食品，并核实每个列表都记录
#  了相应人员喜欢的食品
my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n---------演示不使用切片复制-----------")
my_foods = ['pizza', 'falafel', 'carrot cake']

#  单纯赋值行不通
#  这种语法让Python新变量friend_foods关联到包含在my_foods中的列表，因此
#  两个变量都指向同一个列表，并没有将my_foods的副本存储到friend_foods
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
