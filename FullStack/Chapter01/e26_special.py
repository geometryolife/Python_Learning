# 魔法方法和特殊属性
# 魔法方法也称特殊方法，总是被双下划线包围，如 __init__，特殊属性也是
# 以双下划线包围的属性，如 __dict__ 和 __slots__。
# __dict__ 可以访问类的所有属性，以字典的形式返回
class People(object):
    # 定义构造方法
    def __init__(self, name, age):
        # 初始化类的实例属性
        self.name = name
        self.age = age


people = People('Joe', 22)
print(people.__dict__)
print("name = ", people.__dict__['name'], sep='')
print("age = ", people.__dict__['age'], sep='')
print()


# Python 在新式类中增加了 __slots__ 内置属性，可以把实例属性
# 锁定到 __slot__ 规定的范围内。正常情况下，当定义了一个类，
# 然后创建了一个类的实例后，可以给该实例绑定任何属性和方法，
# 就是动态语言的灵活性。
class Student(object):
    pass


# 动态给实例绑定一个属性
s = Student()
s.name = 'Joe'
print(s.name)


# 注意： __slots__ 定义的属性仅对当前类实例起作用，对继承它的子类不起作用
class Student2(object):
    # __slots__ 属性用元组定义允许绑定的属性名称
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student2('Joe', 25)
print("stu name = {0}, age = {1}".format(stu.name, stu.age))
# stu.score = 90
# AttributeError: 'Student2' object has no attribute 'score'
print()


class Person(object):
    __slots__ = ('name', 'age')
    pass


class Student3(Person):
    pass


ss = Student3()
ss.name = 'Tom'
ss.age = 28
ss.score = 99
print("ss name = {0}, age = {1}, score = {2}".format(
    ss.name, ss.age, ss.score))


# >>> Execution Result:
# {'name': 'Joe', 'age': 22}
# name = Joe
# age = 22

# Joe
# stu name = Joe, age = 25

# ss name = Tom, age = 28, score = 99
