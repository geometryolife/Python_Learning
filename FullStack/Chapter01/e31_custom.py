# 自定义异常
# 使用 raise 关键字抛出自定义异常。
class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    a = 6
    b = 4

    if a > b:
        raise MyException("自定义异常")
except MyException as err:
    print("打印 MyException 异常", err)
except Exception as err:
    print("打印 Excetipn 异常", err)


# >>> Execution Result:
# 打印 MyException 异常 自定义异常
