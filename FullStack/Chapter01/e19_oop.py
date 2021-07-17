# 面向对象程序设计(Object Oriented Programming, OOP)
# 对象 = 数据 + 数据的操作
# 类(class)是对相同类型的对象进行分类、抽象后，得出共同特征的对象抽象，即类
# 是对一群具有相同属性和方法的对象的抽象。
# object 类是所有类的父类

# 定义类
class Car(object):
    # 类属性
    num = 111

    # 类方法
    def info(self):
        print("This is a car.")


# 实例化类
car = Car()
print("Car 类对象的属性 num 为: ", car.num)

# 在类中直接定义的属性也称为类属性，类属性属于类本身，可以
# 通过类名和属性对象进行访问和修改。
Car.num = 222
print("Car 类对象的属性 num 为: ", Car.num)

# 在定义类的方法时，第1个参数必须是 self，self 参数代表将来要创建的
# 对象本身，需要使用类的对象来调用类中定义的方法。
car.info()


# >>> Execution Result:
# Car 类对象的属性 num 为:  111
# Car 类对象的属性 num 为:  222
# This is a car.
