import pandas as pd

print("----------访问 Series 中的元素和索引----------")

# Series 对象的每个元素都有索引，可以像列表一样访问
ser = pd.Series(data=[1, 3, 5, 7], index=['a', 'b', 'c', 'd'])
print(ser, '\n')

# 访问第1个元素
print(ser[0], '\n')

# 输出序列的长度
print(len(ser), '\n')

# 修改序列第1个元素的值为2
ser[0] = 2
print(ser)

print("\n----------通过枚举的方式访问 Series 对象----------")

for i, v in enumerate(ser):
    print("index=", i, ", value=", v, sep='')

print("\n----------直接遍历 Series 对象的值----------")
for i in ser:
    print("value =", i)


# >>> Execution Result:
# ----------访问 Series 中的元素和索引----------
# a    1
# b    3
# c    5
# d    7
# dtype: int64

# 1

# 4

# a    2
# b    3
# c    5
# d    7
# dtype: int64

# ----------通过枚举的方式访问 Series 对象----------
# index=0, value=2
# index=1, value=3
# index=2, value=5
# index=3, value=7

# ----------直接遍历 Series 对象的值----------
# value = 2
# value = 3
# value = 5
# value = 7
