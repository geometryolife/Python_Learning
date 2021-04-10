#  编写两个for循环，将各个食品列表打印出来
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

print("My favorite food are:")
print(my_foods)
for myfood in my_foods:
    print(myfood.title())

print("\nMy friend's foods are:")
print(friend_foods)
for friendfood in friend_foods:
    print(friendfood.title())
