print("----------结合使用函数和while循环----------")
#  让用户能够尽可能容易地退出，每次提示用户输入时，都应提供
#  退出途径。使用break语句，提供简单途径。


def get_formatted_name(first_name, last_name):
    """返回简洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#  ----------结合使用函数和while循环----------

#  Please tell me your name:
#  (enter 'q' at any time to quit)
#  First name: joe
#  Last name: chen

#  Hello, Joe Chen!

#  Please tell me your name:
#  (enter 'q' at any time to quit)
#  First name: q
