# 读取文件
# 打开文件，得到文件句柄并赋值给一个变量
# 其实只需传一个参数，默认模式是 r，默认编码根据系统 locale 确定
file_obj = open('data/test.txt', 'r', encoding='utf-8')

# file_obj.read([size]): 读取文件的全部内容，如果指定 size 参数，
# 每次最多读取 size 字节的内容。
# 通过句柄对文件进行操作
data = file_obj.read()
print(data)

# 关闭文件
file_obj.close()


file_obj = open('data/test.txt', 'r', encoding='utf-8')

# file_obj.readlines([size]): 读取文件的全部行，以列表形式返回。如果
# 指定 size 参数，读取包含 size 行的列表。
for line in file_obj.readlines():
    # 在 for 循环遍历时，每一行结尾默认插入换行符，使用 rstrip() 或 stripe()
    # 删除，并把每行内容打印到控制台
    print(line.strip())

file_obj.close()
print()

# 使用迭代器遍历 file_obj 对象，读取文件的每行内容，这是运行速度最快
# 的方法，它是没有显式地读取文件，而是利用迭代器每次读取下一行。
file_obj = open('data/test.txt', 'r', encoding='utf-8')

for line in file_obj:
    print(line.strip())

file_obj.close()

# 写入文件
file_obj = open('data/test2.txt', 'w', encoding='utf-8')

# 将字符串写入文件
file_obj.write("Hello, Python!\n")
file_obj.close()

file_obj = open('data/test3.txt', 'a')

file_obj.write("Hello, Python!\n")
file_obj.close()


# >>> Execution Result:
# 111
# 222
# 333

# 111
# 222
# 333

# 111
# 222
# 333
