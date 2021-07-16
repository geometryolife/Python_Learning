# 写数据到 CSV 文件
import csv

# 指定参数 newline=''，否则每写入一行记录的后面会多一个空行
with open('data/test2.csv', 'w', newline='') as file_obj:
    writer = csv.writer(file_obj)
    writer.writerow(['a', 'b', 'c'])
    writer.writerow([1, 2, 3])
    writer.writerow([4, 5, 6])
