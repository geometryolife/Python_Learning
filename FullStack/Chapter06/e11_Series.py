import pandas as pd
import numpy as np

print("----------创建 Series----------")

print("\n----------通过一维数组来创建序列----------")
ser = pd.Series([1, 2, 3, 4])
print(ser, '\n')

# Series 对象包含两个主要的属性: index 和 values
print("Series 对象的索引 =", ser.index)
print("Series 对象的数据值 =", ser.values, '\n')

# 当要生成一个指定索引的 Series 对象时，可以设置 Series 对象的 index 属性
ser = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(ser)

print("\n----------使用字典来创建 Series 对象----------")
course = {'python': 80, 'java': 90, 'c++': 85}
ser = pd.Series(course)
print(ser)

print("\n----------自动索引----------")
# 如果自定义了索引，它会自动寻找原来的索引，如果一样就取原来索引对应的值
# 通过 idx1 调整 series 的索引顺序
idx1 = ['java', 'python', 'c++']
ser = pd.Series(course, index=idx1)
print(ser, '\n')

# Series 对象的元素会严格按照给出的 index 构建，只有 index 中含有的键
# 会被使用，如果 data 中缺少相应键的值，那么会显示 NaN 值
idx2 = ['python', 'java', 'perl']
ser = pd.Series(course, index=idx2)
print(ser)

print("\n----------排序----------")
# 使用 np.sort() 函数对 Series 对象进行排序
# 升序排列 Series 对象
ser = pd.Series([1, 2, 3, 4])
print(np.sort(ser))
# 降序排列 Series 对象
print(-np.sort(-ser), '\n')


"""
>>> Execution Result:
----------创建 Series----------

----------通过一维数组来创建序列----------
0    1
1    2
2    3
3    4
dtype: int64

Series 对象的索引 = RangeIndex(start=0, stop=4, step=1)
Series 对象的数据值 = [1 2 3 4]

a    1
b    2
c    3
d    4
dtype: int64

----------使用字典来创建 Series 对象----------
python    80
java      90
c++       85
dtype: int64

----------自动索引----------
java      90
python    80
c++       85
dtype: int64

python    80.0
java      90.0
perl       NaN
dtype: float64

----------排序----------
[1 2 3 4]
[4 3 2 1]
"""
