# 把当前目录下所有扩展名为 ".py" 的文件名写入 pylist.txt 文件中
import os

pyList = os.listdir('.')
fileName = 'data/pylist.txt'
file_obj = open(fileName, 'w')

for fileName in pyList:
    # 查询 FullStack 目录下所有扩展名为 .py 的文件名
    if fileName.endswith('.py'):
        # 把扩展名为 .py 的文件名写入文件中
        file_obj.write(fileName + '\n')

# 关闭文件资源
file_obj.close()
