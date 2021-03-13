print("\n----------简单的if语句----------")
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

print("\n----------if-else语句----------")
#  在通过时执行一个操作，并在没有通过时执行另一个操作
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print("\n----------if-elif-else结构----------")
#  现实世界，很多情况要考虑的情形都超过两个，根据年龄段收费的游乐场
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#  简洁写法：在条件结构中只设置价格，最后使用函数print()打印门票
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

#  需要借助str把int类型的变量转换为字符串类型
print("Your admission cost is $" + str(price) + ".")

print("\n----------使用多个elif代码块----------")
#  假设65岁（含）以上的老人，可以半价
age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

print("\n----------省略else代码块----------")
#  Python并不要求if-elif结构后面必须有else代码块。有些情况，else代码块很有用，
#  有些情况，使用一条elif语句来处理特定的情形更清晰
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
