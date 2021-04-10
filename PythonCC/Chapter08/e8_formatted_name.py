print("----------让实参变成可选的----------")
#  为让中间名变成可选的，可给实参middle_name指定一个默认值——空字符串，
#  并在用户没有提供中间名时不使用这个实参。
#  默认形参移动到形参列表的末尾。


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回简洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#  ----------让实参变成可选的----------
#  Jimi Hendrix
#  John Lee Hooker
