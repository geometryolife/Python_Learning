import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'data/username4.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        # 文件不存在就返回None，这是一种不错的做法，函数要么
        # 返回预期的值，要么返回None，如此能够让我们使用函数
        # 的返回值做简单的测试。
        return None
    else:
        return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'data/username4.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")


greet_user()


# What is your name? Joe
# We'll remember you when you come back, Joe!

# Welcome back, Joe!
