# 私有属性和方法
# 1. 在类的内部可以定义属性和方法，在方法内封装业务逻辑，通过类的对象访问方法。
# 但类的属性既可以在类的内部进行访问和修改，也可以通过类的对象进行访问和修改，
# 这样会破坏数据的封装。
# 2. 如果要让类的属性不能被外部访问，可以在属性的名称前加上两个下划线“__”。
# 3. 如果属性的名称以两个下划线开头，则表示是私有属性。
# 4. 私有属性在类的外部不能直接访问，需要通过调用对象的共有方法来访问。
# 5. 子类可以继承父类的公有成员，但是不能继承其私有成员。
# 6. 私有方法的名称以两个下划线开始，在私有方法中可以访问类的所有属性，只能
# 在类的内部调用私有方法，无法通过对象调用私有方法。
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("name = {0}, age = {1}".format(self.name, self.age))


stu = Student("Tom", 21)
stu.name = "Jim"
stu.info()

# 通过类的实例对象修改属性
stu.age = 25
print("name = {0}, age = {1}".format(stu.name, stu.age))
print()

# 修改 Student 类，把属性 name 和 age 改为私有属性


class Student2(object):
    def __init__(self, name, age):
        # 定义私有属性，私有属性在类外部无法直接进行访问
        self.__name = name
        self.__age = age

    def info(self):
        print("name = {0}, age = {1}".format(self.__name, self.__age))


stu2 = Student2('Joe', 21)
stu2.info()
# print(stu2.__name)
# AttributeError: 'Student2' object has no attribute '__name'
print()


class Student3(object):
    def __init__(self, name, age):
        # 私有属性
        self.__name = name
        self.__age = age

    # 内部增加私有方法 __printFun() 打印学生信息
    def __printFun(self):
        print("name = {0}, age = {1}".format(self.__name, self.__age))

    # 类的共有方法调用私有方法
    def info(self):
        self.__printFun()


stu3 = Student3("Joe", 21)
stu.info()


# >>> Execution Result:
# name = Jim, age = 21
# name = Jim, age = 25

# name = Joe, age = 21

# name = Jim, age = 25
