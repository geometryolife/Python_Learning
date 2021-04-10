print("----------访客名单----------")
# 编写一个while循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印
# 一句问候语，并将一条访问记录添加到文件guest_book.txt中。确保这个文件中
# 的每条记录都独占一行。

filename = 'datadir/guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input("What's your name?(enter 'q' to quit) ")
        if name != 'q':
            file_object.write(name.title() + "\n")
            print("Hello, " + name.title())
        else:
            break
