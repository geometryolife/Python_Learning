# 静态方法
# 静态方法是类中的函数，不需要实例。静态方法主要用来存放逻辑性的代码，
# 主要是一些逻辑属性，但是和类本身没有交互，即在静态方法中，不会涉及类
# 中的方法和属性的操作。静态方法定义的时候使用 @staticmethod 装饰器。
# 静态方法可以通过类名访问，也可以通过实例访问。
# 静态方法不需要创建对象就可以执行类中的方法。
class Car(object):
    @staticmethod
    def description():
        print("This is a car.")


# 通过类名调用静态方法
Car.description()

c1 = Car()
# 通过实例调用静态方法
c1.description()


# >>> Execution Result:
# This is a car.
# This is a car.
