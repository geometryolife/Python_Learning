"""一个可用于描述餐馆的类"""
#  将最新的Restaurant类存储在一个模块中。在另一个文件中，导入
#  Restaurant类，创建一个Restaurant实例，并调用Restaurant的一
#  个方法，以确认import语句正确无误


class Restaurant():
    """模拟一家餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化描述餐馆的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """返回描述餐馆的信息"""
        message = self.restaurant_name.title() + " is a " + \
            self.cuisine_type + " type restaurant."
        return message
