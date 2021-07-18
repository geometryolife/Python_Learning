# 子类可以继承父类中的方法，而不需要重新编写相同的方法。但有时子类并不想原
# 封不动地继承父类的方法，而想做一定的修改，这就需要重写方法。若子类中的方
# 法与父类中的某一方法具有相同的方法名、输入参数和返回类型，则新方法将覆盖
# 原有的方法。
# 如果需要在子类中调用父类原有的方法，可以通过 super().methodName() 的方式
# 进行调用。
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
        People.__init__(self, name, gender)
        # 定义类的本身属性
        self.grade = grade

    def speak(self):
        super().speak()
        print("{0} 说：我的性别是 {1}，在读 {2} 年级".format(
            self.name, self.gender, self.grade))


stu = Student('Joe', 'male', '3')
stu.speak()


# >>> Execution Result:
# Joe 的性别是 male
# Joe 说：我的性别是 male，在读 3 年级
