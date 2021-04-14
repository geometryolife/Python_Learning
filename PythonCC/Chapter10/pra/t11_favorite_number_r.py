import json

print("----------喜欢的数字----------")
# 编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个
# 数字存储到文件中。再编写一个程序，从文件中读取这个值，并打印消息
# "I know your favorite number! It's "。

filename = 'datadir/favorite_number.json'
with open(filename) as f_obj:
    favorite_num = json.load(f_obj)

print("I know your favorite number! I'ts " + favorite_num)
