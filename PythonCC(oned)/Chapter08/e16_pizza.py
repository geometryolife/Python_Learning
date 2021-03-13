print("----------传递任意数量的实参----------")
#  有时候，预先不知道函数需要接受多少个实参，Python允许函数从调用语句
#  中收集任意数量的实参。

#  比如，制作一个比萨，它需要接受很多配料，但无法预先确定顾客要多少种配料

#  形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将
#  接收到的所有值都封装到这个元组中。


def make_pizza1(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


#  Python将实参封装到一个元组中，即便函数只能收到一个值也如此
make_pizza1('pepperoni')
make_pizza1('mushrooms', 'green peppers', 'extra cheese')

print("\n----------遍历----------")
#  将print语句替换为一个循环，对配料列表进行遍历，并对顾客点到比萨进行描述


def make_pizza2(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza2('pepperoni')
make_pizza2('mushrooms', 'green peppers', 'extra cheese')
