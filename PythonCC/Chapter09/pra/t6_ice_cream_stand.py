print("----------冰淇淋小店----------")
#  冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，
#  让它继承练习9-1或练习9-4而编写的 Restaurant 类。添加一个 flavors
#  的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示
#  这些冰淇淋的方法。创建一个 IceCreamStand 实例，并调用这个方法。


class Restaurant():
    """描述一家餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印描述餐馆的信息"""
        print("The restaurnt name is " + self.restaurant_name + ".")
        print("It's a " + self.cuisine_type + " type restaurant.")

    def open_restaurant(self):
        """指出餐馆正在营业"""
        print("This restaurant is open now. Welcome!")


class IceCreamStand(Restaurant):
    """冰淇淋小店的独特之处"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['original', 'double cream',
                        'strawberry', 'matcha', 'fresh orange', 'blueberry']

    def describe_ice_cream(self):
        """显示店里的冰淇淋种类"""
        print("Welcome, what kind of ice cream do you want:")
        for flavor in self.flavors:
            print("- " + flavor.title() + " flavor")


ice_cream_stand = IceCreamStand('粤式冰点', 'cantonese')
ice_cream_stand.describe_restaurant()
ice_cream_stand.describe_ice_cream()


#  ----------冰淇淋小店----------
#  The restaurnt name is 粤式冰点.
#  It's a cantonese type restaurant.
#  Welcome, what kind of ice cream do you want:
#  - Original flavor
#  - Double Cream flavor
#  - Strawberry flavor
#  - Matcha flavor
#  - Fresh Orange flavor
#  - Blueberry flavor
