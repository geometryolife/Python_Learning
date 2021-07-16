import os

# 获取复制文件的大小
fileTotalSize = os.stat('data/photo.jpg').st_size
print("fileTotalSize = {0}".format(fileTotalSize))

# 已读取文件大小
readSize = 0

# 以二进制模式打开并读取一个文件
file_obj = open('data/photo.jpg', 'rb')

# 以二进制模式打开一个文件只用于写入
file_obj2 = open('data/photo3.jpg', 'wb')

# 判断是否已经读取完文件，对读取文件大小和文件总大小进行比较
while readSize < fileTotalSize:
    # 每次读取50 KB 的文件内容
    content = file_obj.read(1024 * 50)
    readSize = readSize + len(content)
    file_obj2.write(content)
else:
    print("fileTotalSize = {0}, readSize = {1}".format(
        fileTotalSize, readSize))

# 关闭文件资源
file_obj.close()
file_obj2.close()

# 解释:
# while 循环中重复调用 file_obj.read(size) 函数，每次读取 size 个字节的文件
# 内容到内存中，然后把文件内容写入目标文件中。在 while 循环中统计每次读取文
# 件内容的大小，然后与文件的大小进行比较，如果统计的读取文件大小与文件总大
# 小一致就停止循环，最后释放文件资源。
