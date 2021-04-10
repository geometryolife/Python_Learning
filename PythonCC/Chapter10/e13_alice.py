print("----------使用多个文件----------")
# 分析多本书时，可将之前的程序封装到一个函数中，使用一个循环来调
# 用这个函数对多本书进行分析。


def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist"
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")


filename = 'data/alice.txt'
count_words(filename)

print("\n----------遍历----------")
filenames = ['data/alice.txt', 'siddhartha.txt', 'data/moby_dict.txt',
             'data/little_women.txt']

for filename in filenames:
    count_words(filename)

# 使用try-except代码块提供了两个重要的优点:
# 1.避免让用户看到traceback；
# 2.让程序能够继续分析能够找到的其他文件；
# 如果不捕获异常，则在找不到文件后，返回traceback并终止程序，无法继续
# 分析后面的文件。
