import json


def get_stored_username():
    """如果存储了用户，就获取它"""
    filename = 'data/username5.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'data/username5.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()


# remember_me.py的最终版，每个函数都执行单一而清晰的任务，要编写出清
# 晰而易于维护的代码和扩展的代码，这种划分工作必不可少。
