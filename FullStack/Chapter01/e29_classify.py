# 异常的分类处理
# 如果想同时使用 Exception 和单个类型异常捕捉，应该把单个类型异常的捕捉放
# 到 Exception 的前面，因为如果把 Exception 作为捕获的第一个异常，那么使用
# Exception 会捕捉所有的异常错误，Exception 下面的单个异常处理就不再执行。
try:
    x = int(input("input x: "))
    y = int(input("input y: "))
    print("x/y = ", x/y)
# 捕捉除0异常
except ZeroDivisionError:
    print("ZeroDivison")
# 捕捉多个异常
except (TypeError, ValueError) as e:
    print(e)
# 捕捉其余类型异常
except Exception:
    print("It's still wrong.")
# 没有异常时执行
else:
    print("It work well")


# >>> Execution Result:
# input x: 10
# input y: 2
# x/y =  5.0
# It work well


# input x: 10
# input y: 0
# ZeroDivison

# input x: 10
# input y: a
# invalid literal for int() with base 10: 'a'
