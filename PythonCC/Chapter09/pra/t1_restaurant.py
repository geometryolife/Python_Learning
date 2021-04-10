#  创建一个名为 Restaurant 的类，其方法__init__()设置两个属性:
#  restaurant_name 和 cuisine_type。创建一个名为describe_restaurant()
#  的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，
#  而后者打印一条消息，指出这个餐馆正在营业。

#  根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再
#  调用前述两个方法。
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


restaurant = Restaurant('港式烧腊', 'cantonese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
