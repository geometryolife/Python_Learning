import json

# 对于用户生成的数据，使用json保存它们大有裨益，因为如果不以某种方式进行
# 存储，等程序停止运行时用户的信息将丢失。

print("----------保存和读取用户生成的数据----------")
# 用户首次运行程序时被提示输入自己的名字，这样再次运行程序时就记住他了。

username = input("What's is your name? ")

filename = 'data/username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
