# 当使用 import 模块名导入一个模块时，Python 会在以下路径中搜索它想要寻找的
# 模块，搜索路径会存放在 system 模块的 sys.path 变量中。
# - 程序所在的文件夹
# - 标准库的安装路径
# - 操作系统环境变量 PYTHONPATH 所包含的路径

import sys

# sys.path 返回一个路径的列表
print(sys.path, '\n')

ps = sys.path
for p in ps:
    print(p)


# 添加自定义的搜索路径
# sys.path.append('引用模块的地址')

# 永久设置模块的搜索路径，需要设置操作系统的环境变量 PYTHONPATH。


# >>> Execution Result:
# ['/home/ubuntu/Python_Learning/FullStack/Chapter01/modulePath',
# '/usr/lib/python38.zip', '/usr/lib/python3.8',
# '/usr/lib/python3.8/lib-dynload',
# '/home/ubuntu/.local/lib/python3.8/site-packages',
# '/usr/local/lib/python3.8/dist-packages',
# '/usr/local/lib/python3.8/dist-packages/cloud_init-20.1-py3.8.egg',
# '/usr/lib/python3/dist-packages']

# /home/ubuntu/Python_Learning/FullStack/Chapter01/modulePath
# /usr/lib/python38.zip
# /usr/lib/python3.8
# /usr/lib/python3.8/lib-dynload
# /home/ubuntu/.local/lib/python3.8/site-packages
# /usr/local/lib/python3.8/dist-packages
# /usr/local/lib/python3.8/dist-packages/cloud_init-20.1-py3.8.egg
# /usr/lib/python3/dist-packages
