print("----------将函数存储在模块中----------")
#  函数的优点之一: 将代码块与主程序分离。

#  模块: 将函数存储在独立的文件中，使用import语句导入主程序

#  将函数存储在独立文件中:
#  1.可隐藏程序代码的细节，将重点放在程序的高层逻辑上。
#  2.可与其他程序员共享这些文件而不是整个程序。

#  学习目标:
#  知道如何导入函数，如何使用其他人编写的函数库。


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
