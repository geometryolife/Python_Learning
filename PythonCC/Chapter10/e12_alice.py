print("----------文本分析----------")

# 方法split()以空格为分隔符将字符串分拆成多个部分，并将
# 这些部分都存储到一个列表中。
title = "Alice in Wonderland"
print(title.split())
# ['Alice', 'in', 'Wonderland']

# 为计算Alice in Wonderland包含多少个单词，我们将对整篇小说调用split()，
# 再计算得到的列表包含多少个元素，从而确定整篇童话大致包含多少单词。

filename = 'data/alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exits."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    # words是一个包含整本书的字符串
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
