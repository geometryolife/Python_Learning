# 从 CSV 文件中读取数据
import csv

# 以列表形式打印每一行
with open('data/test.csv', 'r') as file_obj:
    reader = csv.reader(file_obj)
    # 通过迭代器访问 reader 对象
    for row in reader:
        # 返回列表对象
        print(row)
print()

# 以字符串形式打印每一行
with open('data/test.csv') as file_obj:
    for line in file_obj:
        # 返回一行数据
        print(line.strip())


# >>> Execution Result:
# ['name', 'age', 'address']
# ['Joe', '20', 'ShenZhen']
# ['Tom', '21', 'BeiJing']

# name,age,address
# Joe,20,ShenZhen
# Tom,21,BeiJing
