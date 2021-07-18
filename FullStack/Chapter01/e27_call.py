# 在 Python 中，函数也是一种对象。实际上，任何一个有 __call__() 特殊方
# 法多对象都被当作是函数。
class Add(object):
    def __call__(self, a):
        return a + 5


# 定义函数对象，可以把函数对象看作函数
add = Add()
# 调用函数
print(add(2), '\n')


# 所有的函数都是可调用对象。由于 add 可以被调用，因此 add 被称为可调用对象。一
# 个类实例也可以变成一个可调用对象，只需要实现一个特殊的方法__call__()。
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print("打印类的实例属性 name = {0}, gender= {1}".format(
            self.name, self.gender))
        print("打印 __call__() 方法的参数 friend = {0}".format(friend))


person = Person('Joe', 'male')
person('Tom')

# 解释:
# 仅看 person('Tom') 无法确定 person 是一个函数还是一个类实例。所以在
# Python 中，函数也是对象，对象和函数的区别并不显著，这也是 Python 灵活之处。


# >>> Execution Result:
# 7

# 打印类的实例属性 name = Joe, gender= male
# 打印 __call__() 方法的参数 friend = Tom
