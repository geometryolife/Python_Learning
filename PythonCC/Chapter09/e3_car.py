print("----------给属性指定默认值----------")


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        #  类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

    def update_odometer2(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

    def increment_odometer2(self, miles):
        """
        将里程表读数增加指定的量
        禁止增量为负值，防止将里程表读数往回调
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("你不能回调里程表!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("\n----------直接修改属性的值----------")
#  修改属性的值，最简单的方式是通过实例直接访问它。

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("\n----------通过方法修改属性的值----------")
#  通过方法修改属性的值，无需直接访问属性，而可将值传递给一个方法，
#  由方法在内部进行更新。
my_new_car.update_odometer(35)
my_new_car.read_odometer()

#  添加逻辑，禁止任何人将里程表读数往回调
my_new_car.update_odometer2(23)

print("\n----------通过方法对属性的值进行递增----------")
#  有时候需要将属性值递增特定的量，而不是将其设置为全新的值。
#  假设购买一辆二手车，而且从购买到登记期间增加了100英里的里
#  程，通过方法传递增量，并相应地增加里程表读数。
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_used_car.increment_odometer2(-200)


#  ----------给属性指定默认值----------
#  2016 Audi A4
#  This car has 0 miles on it.

#  ----------直接修改属性的值----------
#  This car has 23 miles on it.

#  ----------通过方法修改属性的值----------
#  This car has 35 miles on it.
#  You cant't roll back an odometer!

#  ----------通过方法对属性的值进行递增----------
#  2013 Subaru Outback
#  This car has 23500 miles on it.
#  This car has 23600 miles on it.
#  你不能回调里程表!
