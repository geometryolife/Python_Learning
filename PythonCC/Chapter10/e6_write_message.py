print("----------写入多行----------")
filename = 'data/programming2.txt'

with open(filename, 'w') as file_object:
    # 方法write()不会在写入的文本末尾添加换行符，因此写入多行时，
    # 需要使用空格、制表符、空行来设置其格式。
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
