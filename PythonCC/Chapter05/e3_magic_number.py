print("----------比较数字----------")
age = 18
print(age == 18)

#  检查是否不等
answer = 17

if answer != 42:
    print("That is not the corret answer. Please try again!")

print("\n----------各种数学比较----------")
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#  if语句中可以使用各种数学比较，这让你能够直接检查关心的条件

print("\n----------使用and检查多个条件----------")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

#  改善可读性，可将每个测试都分别放在一对括号内，但并非必须如此
(age_0 >= 21) and (age_1 >= 21)

print("\n----------使用or检查多个条件----------")
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

print("\n----------关键字in----------")
#  检查特定值是否包含在列表中
requested_toppings = ['mushroom', 'onions', 'pineapple']
print('mushroom' in requested_toppings)
print('pepperoni' in requested_toppings)

print("\n----------not in----------")
#  检查特定的值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

print("\n----------布尔表达式----------")
#  布尔值通常用于记录条件
#  在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式
game_active = True
can_edit = False
