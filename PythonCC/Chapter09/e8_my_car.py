#  导入类是一种有效的编程方式，使主程序文件变得整洁易读，专注程序的高级逻辑
from e7_car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
