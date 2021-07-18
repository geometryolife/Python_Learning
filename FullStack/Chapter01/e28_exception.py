# 错误:
# 在编写程序的时候，错误是难免的，如语法错误、逻辑错误等。
# 当 Python 检测到一个错误时，解释器就无法继续执行下去，抛出相应的错误信息。
# 异常:
# 即便 Python 程序的语法是正确的，在运行的时候也有可能发生错误。运行期检测
# 到的错误被称为异常。出现异常时，程序不会退出，还会正常运行。
# Exception 是一个类
# 异常处理机制可以增强程序的健壮性与容错性。
"""
异常处理语法:
try:
    # 主代码块
    pass
except 异常类型 as e:
    # 异常时，执行该块
    pass
else:
    # 主代码块执行完，执行该块
    pass
finally:
    # 无论异常与否，最终执行该块
    pass
"""

# 简单异常处理
# 处理 invalid 异常
try:
    inp = input("input a int param: ")
    num = int(inp)
    print(num)
except ValueError as e:
    print("抛出异常")
    print(e)

# 如果捕获异常时不想指定异常，想直接捕获所有类型的异常就使用 Exception。
try:
    inp = input("input a int param: ")
    num = int(inp)
    print(num)
except Exception as e:
    print("抛出异常")
    print(e)


# >>> Execution Result:
# input a int param: aaa
# 抛出异常
# invalid literal for int() with base 10: 'aaa'
# input a int param: bbb
# 抛出异常
# invalid literal for int() with base 10: 'bbb'
