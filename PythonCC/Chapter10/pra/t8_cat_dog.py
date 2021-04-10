# 创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，
# 在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，
# 并将其内容打印到屏幕上。将这些代码放在一个try-except代码块中，以便
# 在文件不存在时捕获FileotFound错误，并打印一条友好的消息。将其中一个
# 文件已到另一个地方，并确认except代码块中的代码将正确地执行。
print("----------猫和狗----------")


def show_msg(filename):
    """以行打印文件中的内容"""
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist.")
    else:
        for line in lines:
            print(line.rstrip())


filenames = ['datadir/cats.txt', 'datadir/dogs.txt']
for filename in filenames:
    print()
    show_msg(filename)

filenames = ['cats.txt', 'datadir/dogs.txt']
for filename in filenames:
    print()
    show_msg(filename)
