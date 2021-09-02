import pandas as pd
import numpy as np

print("----------对 Series 对象进行简单运算----------")

# 对数据对象进行选择，如打印大于 81 的 Series 数据
course = {'python': 80, 'java': 90, 'c++': 85}
ser = pd.Series(course)
print(ser[ser > 81], '\n')

# 直接对 Series 对象进行逻辑运算
# 对 Series 对象的每个值乘以 2
print(ser * 2)

print("\n----------查看序列的数据----------")

ser = pd.Series(np.arange(0, 100))

# np.head() 查看序列的前几行数据
print(ser.head(3), '\n')
# np.tail() 查看序列的后几行数据
print(ser.tail(3))


# >>> Execution Result:
# ----------对 Series 对象进行简单运算----------
# java    90
# c++     85
# dtype: int64

# python    160
# java      180
# c++       170
# dtype: int64

# ----------查看序列的数据----------
# 0    0
# 1    1
# 2    2
# dtype: int64

# 97    97
# 98    98
# 99    99
# dtype: int64
