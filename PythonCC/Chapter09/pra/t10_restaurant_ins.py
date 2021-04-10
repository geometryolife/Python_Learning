#  将最新的Restaurant类存储在一个模块中。在另一个文件中，导入
#  Restaurant类，创建一个Restaurant实例，并调用Restaurant的一
#  个方法，以确认import语句正确无误

import t10_restaurant_mod as re

my_restaurant = re.Restaurant('the time', 'continental')
print(my_restaurant.describe_restaurant())
