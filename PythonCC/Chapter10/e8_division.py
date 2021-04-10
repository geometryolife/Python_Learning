print("----------异常----------")
# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。
# 每当发生让Python不知所措的错误时，它都会创建一个异常对象；
# 如果编写了处理该异常的代码，程序将继续运行；
# 如果未对异常进行处理，程序将停止并显示一个traceback，
# 其中包含有关异常的报告。

# 异常使用try-except代码块处理

print("\n----------处理ZeroDivisionError异常----------")
# print(5 / 0)

# Traceback (most recent call last):
# File "e8_division.py", line 11, in <module>
# print(5 / 0)
# ZeroDivisionError: division by zero

print("\n----------使用try-except代码块----------")
# 如果try-except代码块后面还有其他代码，程序将接着运行，因为已经告诉了
# Python如何处理这种错误。

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
