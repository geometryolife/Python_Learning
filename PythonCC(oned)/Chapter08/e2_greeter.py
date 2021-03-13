print("----------向函数传递信息----------")


#  使用函数参数
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")


greet_user('jesse')

print("\n----------实参和形参----------")
#  形参: 函数完成其工作所需的一项信息
#  实参: 调用函数时传递给函数的信息
