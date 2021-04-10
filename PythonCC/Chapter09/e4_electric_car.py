print("----------继承----------")
#  编写类时，并非总是要从空白开始。
#  如果要编写的类是另一个现成类的特殊版本，可使用继承。
#  一个类继承另一个类时，将自动获得另一个类的所有属性和方法；
#  原有的类称为父类，而新类称为子类。
#  子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

print("\n----------子类的方法__init__()----------")
#  模拟电动汽车，在Car类的基础上创建新类ElectricCar


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("你不能回调里程表!")

#  创建子类时，父类必须包含在当前文件中，且位于子类前面，括号内指定父类名称


class ElectricCar(Car):
    """电动汽车的独特之处"""

    #  __init__()接受创建Car实例所需的信息
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        #  super()是一个特殊函数，帮助Python将父类和子类关联起来
        #  让Python调用ElectricCar的父类的方法__init__()，让ElectricCar
        #  实例包含父类的所有属性。
        #  父类也称为超类(superclass)
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
