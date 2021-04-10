# 提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是
# 数字。在这种情况下，当你尝试将输入转换为整数时，将引发ValueError异
# 常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在
# 用户输入的任何一个值不是数字时都捕获ValueError异常，并打印一体友好
# 的错误消息。对编写的程序进行测试:先输入两个数字，再输入一些文本而
# 不是数字。
print("----------加法运算----------")

print("Give me two numbers, and I'll add them.")

try:
    first_num = int(input("\nFirst number: "))
except ValueError:
    print("You must enter a number!")
else:
    try:
        second_num = int(input("Second number: "))
    except ValueError:
        print("You must enter a number!")
    else:
        answer = first_num + second_num
        print(answer)
