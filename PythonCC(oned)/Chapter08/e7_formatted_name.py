print("----------让实参变成可选的----------")


#  处理中间名
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
