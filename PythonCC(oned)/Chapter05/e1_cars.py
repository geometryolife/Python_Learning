print("---------简单示例-----------")
#  遍历一个列表，并以首字母大写的方式打印其中的汽车名，但对于汽车名
#  'bmw'，以全大写的方式打印
cars = ['audi', 'bmw', 'subaru', 'toyoto']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("\n---------测试条件-----------")

#  测试条件: 每条if语句的核心都是一个值为True或False的表达式，这种
#  表达式称为测试条件

#  检查是否相等
car = 'audi'
print(car == 'audi')

car = 'audi'
print(car == 'bmw')

#  检查是否相等时不考虑大小写
car = 'Audi'
print(car == 'audi')

#  如果大小写很重要，这种行为有其优点
#  如果大小写无关紧要，而只想检查变量的值，可将变量值转换为小写
car = 'Audi'
print(car.lower() == 'audi')

#  函数lower()不会修改存储在变量car中的值
print(car)
