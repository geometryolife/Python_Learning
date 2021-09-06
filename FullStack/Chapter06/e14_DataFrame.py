import numpy as np
import pandas as pd

print("----------创建 DataFrame----------")
# 使用列表创建 Pandas 的 DataFrame 对象
data1 = ['a', 'b', 'c']
df = pd.DataFrame(data1)
print(df, '\n')

# 使用嵌套的列表创建 Pandas 的 DataFrame 对象
data2 = [['a', 'b', 'c'], ['d', 'e', 'f']]
df = pd.DataFrame(data2)
print(df, '\n')

print("\n----------使用字典创建 DataFrame 对象----------")
data = {
    'name': ['baidu', 'taobao', '163'],
    'marks': [100, 101, 102],
    'price': [9, 3, 7]
}
df = pd.DataFrame(data)
print(df, '\n')

# 改变 DataFrame 的 columns 属性的顺序
df = pd.DataFrame(data, columns=['marks', 'name', 'price'])
print(df, '\n')

# 创建 DataFrame 对象时，自定义 index 属性的值
df = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df)

print("\n----------使用 NumPy 的随机函数生成矩阵----------")
# 生成一个3行4列的 df
df = pd.DataFrame(np.random.randn(3, 4))

# 对 DataFrame 的行索引赋值
df.index = ['a', 'b', 'c']

# 对 DataFrame 的列索引赋值
df.columns = ['a', 'b', 'c', 'd']
print(df)


"""
>>> Execution Result:
----------创建 DataFrame----------
   0
0  a
1  b
2  c

   0  1  2
0  a  b  c
1  d  e  f


----------使用字典创建 DataFrame 对象----------
     name  marks  price
0   baidu    100      9
1  taobao    101      3
2     163    102      7

   marks    name  price
0    100   baidu      9
1    101  taobao      3
2    102     163      7

     name  marks  price
a   baidu    100      9
b  taobao    101      3
c     163    102      7

----------使用 NumPy 的随机函数生成矩阵----------
          a         b         c         d
a -0.161311  0.741804 -0.339858  0.686970
b -0.481736 -0.707678  0.118119 -0.387795
c  0.247714  0.749358  0.105579 -0.652826
"""
