print("----------在字典中存储列表----------")
#  存储所有点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#  概述所有点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#  每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表
