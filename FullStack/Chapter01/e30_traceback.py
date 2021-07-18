# 使用 traceback 模块捕获并打印异常，traceback 模块用来精确模仿 Python 解
# 释器的 stack trace 行为。在程序中应该尽量使用这个模块，可以在控制台更直
# 观地显示异常。
import traceback

try:
    print(1/0)
except Exception:
    # 直接打印当前异常
    traceback.print_exc()


"""
>>> Execution Result:
Traceback (most recent call last):
  File "e30_traceback.py", line 7, in <module>
    print(1/0)
ZeroDivisionError: division by zero
"""
