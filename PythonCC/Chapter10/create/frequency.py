import jieba


def WordQ(filepath, m):
    with open(filepath, m) as sg:
        txt = sg.read()
        words = jieba.lcut(txt)
        counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[-1], reverse=True)
    for i in range(20):
        word, counts = items[i]
        print("{0:<10} {1:>5}".format(word, counts))
    # WordQ.close()


WordQ('../data/alice.txt', 'r')
