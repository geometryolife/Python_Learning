print("----------失败时一声不吭----------")


def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # pass语句充当了占位符
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")


filenames = ['data/alice.txt', 'siddhartha.txt', 'data/moby_dict.txt',
             'data/little_women.txt']

for filename in filenames:
    count_words(filename)

# 并非每次捕获到异常时都需要告诉用户，有时希望程序在发生异常时
# 静默地继续运行。那么只需要在except代码块中使用pass语句让
# Pyton什么都不要做。

# pass语句充当了占位符，它提醒你在程序中某个地方什么都没有做，
# 并且以后也许要在这里做些什么。

print("\n----------决定报告哪些错误----------")
# 向用户显示他不想看到的信息可能会降低程序的可用性。
# Python的错误处理结构能够细致地控制与用户分享错误信息的程度。

# Tips:
# 编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，
# 但只要程序依赖于外部因素，如用户输入、存在指定的文件、有网路链接，
# 就有可能出现异常。凭借经验可判断在程序的什么地方包含异常处理块，以及
# 出现错误时该向用户提供多少相关的信息。
