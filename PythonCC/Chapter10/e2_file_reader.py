print("----------逐行读取----------")
#  读取文件时，常常需要检查其中的每一行，可能要在文件中查找特定的信息，
#  或者要以某种方式修改文件中的文本。

#  将要读取的文件的名称存储在变量中，是使用文件的一种常见的做法。
filename = 'data/pi_digits.txt'

with open(filename) as file_object:
    #  要以每次一行的方式检查文件，可对文件对象使用for循环。
    for line in file_object:
        #  每行的末尾都有一个看不见的换行符，而print语句也会加上一个换行符，
        #  因此每行末尾都有两个换行符。
        print(line)

print("\n----------去除空行----------")
with open(filename) as file_object:

    for line in file_object:
        print(line.rstrip())
