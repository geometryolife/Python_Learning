from random import randint

print("----------骰子----------")
# 模块random包含以各种方式生成随机数的函数，其中的randint()返回一
# 个位于指定范围内的读数，例如，下面的代码返回一个1~6内的整数:
# from random import randint
# x = randint(1, 6)

# 请创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。
# 编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机
# 数。创建一个6面的骰子，再掷10次。
# 创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。


class Die():
    """模拟骰子"""

    def __init__(self, sides):
        """初始化骰子的面数"""
        self.sides = sides

    def roll_die(self):
        """打印掷得的骰子数"""
        x = randint(1, self.sides)
        print("骰子点数是: " + str(x))


# 创建一个6面的骰子，投掷10次
dice1 = Die(6)
# 让骰子掷10次
current_number = 1
while current_number <= 10:
    dice1.roll_die()
    current_number += 1

print("\n----------改进----------")
# 使用变量来控制掷骰子的次数
times = 10
while times > 0:
    dice1.roll_die()
    times -= 1

print("\n----------面数更多的骰子----------")
# 创建一个10面的骰子和一个20面的骰子，并将它们都掷10次
print("10面的骰子掷10次:")
times = 10
dice10 = Die(10)
while times > 0:
    dice10.roll_die()
    times -= 1

print("\n20面的骰子掷10次:")
times = 10
dice20 = Die(20)
while times > 0:
    dice20.roll_die()
    times -= 1
