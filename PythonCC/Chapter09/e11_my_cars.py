from e9_car import Car, ElectricCar
print("----------从一个模块中导入多个类----------")

#  创建一辆大众甲壳虫普通汽车
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

#  创建一辆特斯拉Roadster电动汽车
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

#  如果模块中有print()函数，那么在导入模块的时候会自动调用
