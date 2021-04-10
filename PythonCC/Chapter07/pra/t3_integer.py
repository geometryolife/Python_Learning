print("----------10的整数倍----------")

# 让用户输入一个数字，并指出这个数字是否是10的整数倍。
number = input("Please enter a number: ")

if int(number) % 10 == 0:
    print("Oh! You enter " + number + ". It's an integer of ten.")
else:
    print("You enter " + number + ".")
