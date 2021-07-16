# 在执行 file_obj.read() 从文件中读取数据时，有可能产生 IOError 异常。一旦
# 出错，后面的 file_obj.close() 就不会执行，所以为了保证无论是否出错都能正
# 常关闭文件，可以使用 try...finally 来实现异常处理。
try:
    file_obj = open('data/test.txt', 'r', encoding='utf-8')
    data = file_obj.read()
finally:
    if file_obj:
        file_obj.close()

# 上面的代码虽然良好，但是太冗长了。Python 引入了 with 语句自动执行
# file_obj.close() 来释放文件资源。
with open('data/test.txt', 'r', encoding='utf-8') as file_obj:
    data = file_obj.read()

with open('data/test3.txt', 'a', encoding='utf-8') as file_obj:
    file_obj.write("Hello, Joe!")
