print("----------三家餐馆----------")


#  使用练习9.1的类创建三个实例，并对每个实例调用方法describe_restaurant()
class Restaurant():
    """描述一家餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印描述餐馆的信息"""
        print("The restaurant_name is " + self.restaurant_name + ".")
        print("It's a " + self.cuisine_type + " type restaurant.")

    def open_restaurant(self):
        """指出餐馆正在营业"""
        print("This restaurant is open now. Welcome!")


restaurant1 = Restaurant('广东老鸡汤', 'cantonese')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('风雷火重庆火锅', 'Chonging')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('French Style', 'french')
restaurant3.describe_restaurant()
