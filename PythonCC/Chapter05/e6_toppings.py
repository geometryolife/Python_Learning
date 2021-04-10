print("----------使用if语句处理列表----------")
#  检查列表中的特殊值
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#  借助for循环来为比萨添加配料，不必每次加料时都使用print()函数，更高效
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

print("\n----------青椒用完了----------")
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

print("\n----------确定列表不是空的----------")
#  列表为空，询问顾客是否确实要点普通比萨
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")

print("\n----------使用多个列表----------")
#  面对顾客五花八门的要求，利用列表和if语句来确定能否满足顾客的要求
#  第一个列表含比萨店提供的配料，而第二个列表包含顾客点的配料
#  对于requested_toppings中的每个元素，都检查它是否是比萨店供应的
#  配料，再决定是否在比萨中添加它
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
