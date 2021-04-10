import e9_car
print("----------导入整个模块----------")
#  导入整个模块，使用句点表示法访问需要的类，简单易读。
#  创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。

#  这种方式适合从一个模块中导入多个类，既能清楚地知道在程序哪些地方
#  使用了导入的模块，还能避免导入模块中的每个类可能引发的名称冲突

my_beetle = e9_car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = e9_car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


#  ----------在一个模块存储多个类----------
#  ----------导入整个模块----------
#  2016 Volkswagen Beetle
#  2016 Tesla Roadster

print("\n----------导入模块中的所有类----------")
#  from e9_car import *
#  此导入方式的缺点:
#  1. 没有明确指出使用了模块中的哪些类
#  2. 引发难以诊断的错误
