print("\n----------词汇表2----------")
#  使用for循环遍历字典
glossaries = {
    '字典': '一系列键-值对',
    '条件测试': '值为True或False的表达式',
    '列表': '一系列按特定顺序排列的元素组成',
    '元组': '不可变的列表，一系列按特定顺序排列的元素',
    '切片': '对象的子集，处理对象(列表、元组)的部分元素',
}

for k, v in glossaries.items():
    print(k + ": " + v)