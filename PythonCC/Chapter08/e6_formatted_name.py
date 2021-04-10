print("----------返回值----------")
#  函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或
#  一组值。函数返回的值被称为返回值。
#  返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

#  简单的函数，接受名和姓并返回整洁的姓名


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#  应用：在需要存储大量名和姓的大型程序中，像get_formatted_name()
#  这样的函数非常有用。
#  分别存储名和姓，每当需要显示姓名时都调用这个函数。
