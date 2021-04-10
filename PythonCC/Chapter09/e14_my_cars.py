from e13_electric_car import ElectricCar
from e7_car import Car
print("----------在一个模块中导入另一个模块----------")
#  有时需要将类分散到多个模块中，避免规模太大，类不相关。
#  一个模块中的类依赖另一个模块中的类，可在前一个模块中导入必要的类

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
