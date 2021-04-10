print("----------遍历所有的键-值对----------")
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

#  for循环遍历字典
#  遍历字典时，借助两个临时变量存储键和值
#  方法items()返回一个键值对列表
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("\n----------简化变量----------")
for k, v in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
