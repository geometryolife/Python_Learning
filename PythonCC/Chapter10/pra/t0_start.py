import os
print("----------创建存放数据的目录----------")


def create_path(path):
    """创建目录文件夹"""
    is_exist = os.path.exists(path)

    # 如果路径不存在，则创建
    if not is_exist:
        os.mkdir(path)


create_path('datadir')
