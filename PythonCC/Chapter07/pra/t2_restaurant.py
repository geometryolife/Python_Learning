# 编写一个程序，询问用户有多少人用餐。如果超过8人，就
# 打印一条消息，指出没有空桌；否则指出有空桌。
message = input("How many members need to serve? ")

if int(message) > 8:
    print("Sorry, ther are no spare seats.")
else:
    print("There is an empty table here, please!")
