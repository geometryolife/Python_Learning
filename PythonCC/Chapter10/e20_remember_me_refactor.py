import json

print("----------重构----------")
# 代码能够正确地运行，但可做进一步的改进--将代码划分为一系列完成具体工作
# 的函数。此过程被称为重构。

# 重构的优点:
# 让代码更清晰、更易于理解、更容易扩展。

# remember_me.py的重点是问候用户，因此我们将其所有代码都放到一个名为
# greet_user()的函数中


def greet_user():
    """问候用户，并指出其名字"""
    filename = 'data/username3.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")


greet_user()
