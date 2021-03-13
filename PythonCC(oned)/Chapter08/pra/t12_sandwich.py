print("----------三明治----------")
#  编写一个函数，它接受顾客要在三明治中添加的一些列食材。这个函数
#  只有一个形参(它收集函数调用中提供的所有食材)，并打印一条消息，
#  对顾客的三明治进行概述。调用这个函数三次，每次都提供不同数量的
#  实参。


def make_sandwich(*toppings):
    """概述要制作的sandwich"""
    if toppings:
        print("\nMaking a sandwich with the following toppings:")
        for topping in toppings:
            print("- " + topping)
    else:
        print("\nAre you sure you want a plain pizza?")


make_sandwich()
make_sandwich('pepperoni')
make_sandwich('mushroom', 'green peppers', 'extra cheese')
