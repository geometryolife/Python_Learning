# 二进制文件: 图片、音频和视频格式的文件。
# 复制 photo.jpg 图片，命名为 photo2.jpg
# Step1: 以二进制模式打开一个文件只用于读取
file_obj = open('data/photo.jpg', 'rb')

content = file_obj.read()
file_obj.close()

# Step2: 以二进制模式打开一个文件只用于写入
file_obj2 = open('data/photo2.jpg', 'wb')

file_obj2.write(content)
file_obj2.close()

# 解释:
# 运行脚本即可实现图片的复制操作，本例仅仅实现了复制文件的基本功能，还可以
# 进行性能上的优化。使用 file_obj。read() 读取了文件的全部内容到内存，
# 本例读取的文件只有138 KB，这是没问题的。如果文件有13.9 GB，那么一次性全部
# 读入文件内容就可能会导致 MemoryError 异常，也就是内存溢出异常。
# 为了避免内存溢出，需要优化代码，重复调用 file_obj.read(size) 函数，指定每
# 次最多读取 size 个字节的文件内容。size 参数可以根据业务需要进行调整，设置
# 一个合理的值，就可以避免一次性读取大文件的问题。
