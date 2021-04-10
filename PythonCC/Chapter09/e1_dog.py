print("----------创建Dog类----------")


#  类的首字母大写
#  类定义的的括号是空的，即从空白创建这个类
class Dog():
    """一次模拟小狗的简单尝试"""

    #  类中的函数称为方法
    #  方法名前后有双下划线，Python约定俗成表示特殊方法的方式
    #  目的是避免Python默认方法与普通方法发生名称冲突

    #  __init__()的形参self必不可少，且必须位于其他形参的前面

    #  为何必须在方法定义中包含形参self?
    #  Python调用__init__()方法来创建实例，将自动传入实参self。每个
    #  与类相关联的方法调用都自动传递实参self，它是一个指向实例本身
    #  的引用，让实例能够访问类中的属性和方法。

    def __init__(self, name, age):
        """初始化属性name和age"""
        #  以self为前缀的变量都可供类中的所有方法使用，还可以通过
        #  类的任何实例来访问这些变量。

        #  self.name = name获取存储在形参name中的值并将其存储到变
        #  量name中，然后该变量被关联到当前创建的实例。

        #  像这样可通过实例访问的变量称为属性
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


print("\n----------根据类创建实例----------")
#  Python使用实参'willie'和6调用Dog类中的方法__init__()，方法
#  __init__()创建一个表示特定小狗的示例，并使用我们提供的值来
#  设置属性name和age。

#  方法__init__()并未显式地包含return语句，但Python自动返回一个
#  表示这条小狗的实例。
my_dog = Dog('willie', 6)

#  访问属性:
#  访问实例的属性，使用句点表示法
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#  调用方法:
#  创建实例后，可以使用句点表示法来调用Dog类中定义的任何方法
my_dog.sit()
my_dog.roll_over()

print("\n----------创建多个实例----------")
my_dog = Dog('willie', 6)
your_dog = Dog('Lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


#  ----------创建Dog类----------

#  ----------根据类创建实例----------
#  My dog's name is Willie.
#  My dog is 6 years old.
#  Willie is now sitting.
#  Willie rolled over!

#  ----------创建多个实例----------
#  My dog's name is Willie.
#  My dog is 6 years old.
#  Willie is now sitting.

#  Your dog's name is Lucy.
#  Your dog is 3 years old.
#  Lucy is now sitting.


#  Python2.7中创建类，区别:
#  class ClassName(object):
#  class Dog(object):
