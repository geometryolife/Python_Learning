print("----------将实例用作属性----------")


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        将里程表读数增加指定的量
        禁止增量为负值，防止将里程表读数往回调
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("你不能回调里程表!")


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    #  形参使用默认值，使其可选
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a ", str(self.battery_size) + "-kWh battery.")

    #  再给Battery类添加一个方法，它根据电瓶容量报告汽车的续航里程
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range_num = 240
        elif self.battery_size == 85:
            range_num = 270

        message = "This car can go approximately " + str(range_num)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        #  在ElectricCar类中添加self.battery属性，将Battery的实例存储在该属性中
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

#  在实例my_tesla中查找属性battery，并对存储在该属性中的Battery实例调用
#  方法describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#  看似做了很多额外的工作，但现在想多么详细地描述电瓶都可以，
#  而且不会导致ElectricCar类混乱不堪。

#  ----------将实例用作属性----------
#  2016 Tesla Model S
#  This car has a  70-kWh battery.
#  This car can go approximately 240 miles on a full charge.
