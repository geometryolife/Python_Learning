print("----------访客----------")
# 编写一个程序，提示用户输入其名字；用户做出响应后，将其
# 名字写入到文件guest.txt中。


def get_name():
    """获取用户的姓和名，并返回全名"""
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")

    full_name = first.title() + " " + last.title()

    return full_name


def guest():
    """将获取的客人名字写入文件中"""
    name = get_name()

    filename = 'datadir/guest.txt'

    with open(filename, 'w') as file_object:
        file_object.write(name)


guest()
