print("----------使用标志----------")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#  简化了while语句，不需要在其中做任何比较，相关逻辑由其他部分处理。
#  使用一个标志来指出程序是否处于活动状态，如果要添加测试(如elif语句)以检
#  查是否发生了其他导致active变为False的事件，将很容易。
