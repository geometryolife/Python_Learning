import pandas as pd

print("----------查看 DataFrame 信息----------")
data = {
    'name': ['baidu', 'taobao', '163'],
    'marks': [100, 101, 102],
    'price': [9, 3, 7]
}
df = pd.DataFrame(data)
print(df, '\n')

# DataFrame 对象有3个重要的属性，即 df.index、df.columns、df.values
# 获取行索引信息
print(df.index, '\n')

# 获取列索引信息
print(df.columns, '\n')

# 查看 DataFrame 的值
print(df.values, '\n')

# 获取 df 的 size
print(df.shape, '\n')

# 获取 df 的行数
print(df.shape[0], '\n')

# 获取 df 的列数
print(df.shape[1])
