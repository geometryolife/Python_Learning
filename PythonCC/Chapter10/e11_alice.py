print("----------处理FileNotFoundError异常----------")
# 使用文件时，一种常见的问题是找不到文件

# filename = 'alice.txt'

# with open(filename) as f_obj:
# contents = f_obj.read()


# ----------处理FileNotFoundError异常----------
# Traceback (most recent call last):
# File "e11_alice.py", line 6, in <module>
# with open(filename) as f_obj:
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

print("\n----------使用异常处理----------")
filename = 'alice.txt'


try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
