# 改进练习10-6中编写的代码，放在一个while循环中，让用户犯错
# (输入的是文本而不是数字)后能够继续输入数字。
print("----------加法计算器----------")

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

active = True
while active:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    else:
        try:
            first_num = int(first_num)
        except ValueError:
            print("Sorry, you must enter a number!")
            active = False

    if active:
        second_num = input("Second number: ")
        if second_num == 'q':
            break
        else:
            try:
                second_num = int(second_num)
            except ValueError:
                print("Sorry, you must enter a number!")
                active = False

    # 时刻注意字符串相加是拼接
    # answer = first_num + second_num
    if active:
        answer = first_num + second_num
        print(answer)
