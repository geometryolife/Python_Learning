import json

print("----------使用json.load()读取JSON文件----------")

filename = 'data/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# json.dump()和json.load()是一种在程序之间共享数据的简单方式。
