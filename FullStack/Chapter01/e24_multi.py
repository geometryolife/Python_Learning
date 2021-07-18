# 多继承
# 注意: 多继承时，如果父类有相同的方法名，而在子类中使用时没有指定父类
# 名，则 Python 解释器将从左向右顺序进行搜索，即方法在子类中未找到时，
# 从左到右查找父类中是否包含方法。

# 定义父类 Animal1
class Animal1:
    def __init__(self):
        print("creating an animal1")

    def run(self):
        print("running ...")

    def jump(self):
        print("jump from Animal1")

# 定义父类 Animal2


class Animal2:
    def __init__(self):
        print("creating an animal2")

    def eat(self):
        print("eating ...")

    def jump(self):
        print("jump from Animal2")

# 定义子类继承两个父类


class Pig(Animal1, Animal2):
    def __init__(self):
        print("creating a pig")

    def cry(self):
        print("crying ...")


pig = Pig()
pig.cry()
pig.eat()
pig.jump()


# >>> Execution Result:
# creating a pig
# crying ...
# eating ...
# jump from Animal1
