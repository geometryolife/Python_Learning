print("----------附加到文件----------")
# 如果要给文件添加内容，而不是覆盖原有的内容，可以使用附加模式打开文件。
filename = 'data/programming2.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
