print("----------比萨配料----------")

# 编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时
# 结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨
# 中添加这种配料。
prompt = "What would you like to add to the pizza, please? "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print("Adding " + message + ".")
    else:
        print("Finished making your pizza!")
