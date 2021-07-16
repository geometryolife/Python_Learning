# 使用 with 语句读取 test3.txt 文件，读取一行内容，统计文件中有多少行
with open('data/test3.txt', 'r', encoding='utf-8') as file_obj:
    print(file_obj.read())
    # 让文件对象的指针回到开头
    file_obj.seek(0)
    # 统计文件有多少行
    print('rows: %d' % len(file_obj.readlines()), '\n')

# 使用 with 语句读取 test3.txt 文件，输出 test3.txt 中每一行的内容
with open('data/test3.txt') as file_obj:
    for content in file_obj.readlines():
        print(content.strip())

# >>> Execution Result:
# Hello, Python!
# Hello, Python!
# Hello, Python!
# Hello, Python!
# Hello, Python!
# Hello, Joe!
# rows: 6

# Hello, Python!
# Hello, Python!
# Hello, Python!
# Hello, Python!
# Hello, Python!
# Hello, Joe!
