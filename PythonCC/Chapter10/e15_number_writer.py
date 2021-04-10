import json

print("----------存储数据----------")
# JSON(JavaScript Object Notation)格式最初是为JavaScript开发的，但
# 随后成了一种常见格式，被包括Python在内的众多语言采用。


numbers = [2, 3, 5, 7, 11, 13]

filename = 'data/numbers.json'
with open(filename, 'w') as f_obj:
    # 函数json.dump()接受两个实参: 要存储的数据以及可用于存储数据的文件对象。
    json.dump(numbers, f_obj)
