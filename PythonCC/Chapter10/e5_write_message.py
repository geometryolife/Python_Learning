print("----------写入空文件----------")
# 要将文本写入文件，在调用open()时需要提供另一个实参。
# 第一个实参指定要打开的文件的名称；
# 第二个实参指定要以什么模式打开文件。

# 读取模式('r')
# 写入模式('w')
# 附加模式('a')
# 读取和写入文件的模式('r+')

filename = 'data/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# 注意:
# 1. Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，
# 必须先使用函数str()将其转换为字符串格式。
# 2. 以写入('w')模式打开文件时千万要小心，因为如果指定的文件已经存在，
# Python将在返回文件对象前清空该文件。
