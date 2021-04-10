# 运行程序时，尝试从username.json中获取文件名，因此首先编写一个尝试恢
# 复用户的try代码块。如果这个文件不存在，我们就将在except代码块中提示
# 用户输入用户名，并将其存储在username.json中，以便程序再次运行时能够
# 获取它。

import json

# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename = 'data/username2.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
