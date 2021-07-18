# 在 lib 目录里没有 __init__.py 文件时，必须使用下面这条导入语句
# from lib.mod1 import hello
from lib.mod2 import world

# 在 lib 目录里添加了 __init__.py 文件，并添加了相应的 import 语
# 句，可以使用如下导入语句
from lib import hello


hello()
world()
