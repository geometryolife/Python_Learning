print("----------else代码块----------")
# 将可能引发错误的代码放在try-except代码块中，依赖于try代码块成功
# 执行的代码都应放到else代码块中。

print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# 通过预测可能发生错误的代码，可编写健壮的程序，它们即便面临无效数据或缺
# 少资源，也能继续运行，从而能够抵御无意的用户错误和恶意的攻击。

# ----------else代码块----------
# Give me two number, and I'll divide them.
# Enter 'q' to quit.

# First number: 5
# Second number: 0
# You can't divide by 0!

# First number: 5
# Second number: 2
# 2.5

# First number: q
