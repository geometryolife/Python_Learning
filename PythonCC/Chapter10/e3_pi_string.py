print("----------创建一个包含文件各行内容的列表----------")
# 注意:
# 使用关键字with()时，open()返回的文件对象只在with代码块内可用

# 如果要在with代码块外访问文件的内容，可以在with代码块内
# 将文件的各行存储在一个列表中，即可在with代码块外使用该列表。
filename = 'data/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("\n----------使用文件内容----------")
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

print("\n----------同时去除左右两边的空格----------")
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

print("\n----------转换----------")
# 读取文本文件时，Python将其中的所有文本都解读为字符串，若要使用数值，
# 则需要数值转换的函数，int()、float()
print(type(pi_string))

pi_number = float(pi_string)
print(pi_number)
print(type(pi_number))

# 注意:
# 数值字符串的转换必须使用合适的函数，否则报值错误。

# Traceback (most recent call last):
# File "e3_file_reader.py", line 36, in <module>
# pi_number = int(pi_string)
# ValueError: invalid literal for int() with
# base 10: '3.141592653589793238462643383279'
