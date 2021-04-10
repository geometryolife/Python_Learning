print("----------让用户选择何时退出----------")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    #  不打印"quit"
    if message != 'quit':
        print(message)
