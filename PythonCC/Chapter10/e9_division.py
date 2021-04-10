print("----------使用异常避免崩溃----------")
# 发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。

# 异常经常发生在要求用户输入的过程中；如果程序能够妥善地处理无效输入，
# 就能再提示用户提供有效输入，而不至于崩溃。
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# 程序崩溃导致不懂技术的用户会被traceback搞糊涂，怀有恶意的用户
# 会通过traceback获悉你不希望他知道的信息。通过traceback将知道程
# 序文件的名称，还将看到部分不能正确运行的代码。训练有素的攻击者
# 可根据这些信息判断出对你的代码发起什么样的攻击。
