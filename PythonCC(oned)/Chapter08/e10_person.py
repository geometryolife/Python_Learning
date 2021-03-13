print("----------返回字典----------")
#  新增一个可选形参age，并将其默认值设置为空字符串。
#  如果函数调用中包含这个形参的值，这个值将存储到字典中。
#  在任何情况下，这个函数都会存储人的姓名，但可对其进行修改，使其
#  也存储有关人的其他信息。


def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
#  musician = build_person('Joe', 'Chen', 24)

print(musician)

#  ----------返回字典----------
#  {'first': 'jimi', 'last': 'hendrix', 'age': 27}
