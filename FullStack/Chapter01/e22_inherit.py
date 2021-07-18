# 继承: 代码复用，父类(基类) -> 子类(派生类)，支持单继承和多继承。
# Python 中子类继承父类时，在子类的构造函数中调用父类的构造函数有两种写法:
# 经典类: 父类.__init__(self, 参数1, 参数2, ...)
# 新式类: super(子类, self).__init__(参数1, 参数2, ...)
# 单继承
class People(object):
    # 定义构造方法
    def __init__(self, name, gender):
        # 实例属性
        self.name = name
        self.gender = gender

    def speak(self):
        print("{0} 的性别是 {1}".format(self.name, self.gender))


class Student(People):
    def __init__(self, name, gender, grade):
        # 子类重写而屏蔽了 __init__() 方法，继承时使用相应的方式继承父类属性
        # 调用父类的构造方法，也可以写成 People.__init__(self, name,gender)
        super(Student, self).__init__(name, gender)

        # 定义类的本身属性
        self.grade = grade

    def info(self):
        print("{0} 说：我的性别是 {1}，在读 {2} 年级".format(
            self.name, self.gender, self.grade))


stu = Student('Joe', 'male', 3)
stu.speak()
stu.info()


# >>> Execution Result:
# Joe 的性别是 male
# Joe 说：我的性别是 male，在读 3 年级
