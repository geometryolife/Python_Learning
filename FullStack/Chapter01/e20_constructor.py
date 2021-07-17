# 构造方法
# Python 中类的构造函数是 __init__()，一般用来为类的属性设置初值或进行其他
# 必要的初始化工作，在创建对象时被自动调用和执行。如果用户没有设计构造函数，
# Python 将提供一个默认的构造函数来进行必要的初始化工作。
# __init__() 方法的第1个参数是self，表示创建的实例本身。
# __init__() 方法中定义的属性是实例属性，用于记录该对象的特别信息。在类的
# 方法中通过 self 属性的方式获得在 __init__() 方法中初始化的属性值。
class People(object):
    # 定义构造方法
    def __init__(self, name, gender):
        # 实例属性
        self.name = name
        self.gender = gender

    def speak(self):
        """ people can speak """
        print("{0} 的性别是 {1}".format(self.name, self.gender), '\n')


# OOP 的一个重要特点是数据封装，在 People 类的 __init__() 方法中初始化的
# 实例属性 name 和 gender，可以在类的方法中通过类的对象访问类的实例属性。
# 初始化对象
people = People('Tom', 'Male')
people.speak()

people.name = "Lucy"
people.gender = "female"
print("name = {0}, gender = {1}".format(people.name, people.gender))


# >>> Execution Result:
# Tom 的性别是 Male

# name = Lucy, gender = female
