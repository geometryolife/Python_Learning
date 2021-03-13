print("----------传递列表----------")
#  假设有一个用户列表，我们要问候其中的每位用户


def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'try', 'margot']
greet_users(usernames)
