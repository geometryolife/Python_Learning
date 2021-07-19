# Python 的 time 模块下有很多函数可以转换常见日期格式
# 获取当前时间戳
# 使用 time 模块的 time() 函数用于获取当前时间戳，返回当前时间的时间戳。
# 时间戳以自1970年1月1日午夜到当前时间经过了多长时间来表示，是以秒为单
# 位的浮点小数。
import time

ticks = time.time()
print("当前时间戳为：", ticks, '\n')

# 获取当前时间
# 使用 time 模块的 localtime() 函数的作用是格式化时间戳为当前的本地时间
print("获取当前时间 = ", time.localtime())
print("获取当前时间 = ", time.ctime(), '\n')

# 格式化日期
# 使用 strftime() 函数来格式化日期
# time.strftime(format[, t])
# format 格式日期的字符串
# t 可选的参数，是一个 struct_time 对象

# 格式化日期的格式为 年-月-日 小时:分钟:秒
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '\n')

# 推迟线程的运行
# sleep(seconds) 函数推迟调用线程的运行，可通过参数 seconds 指
# 秒数，表示进程挂起的时间
print("开始时间: {0}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
time.sleep(5)
print("结束时间: {0}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


# >>> Execution Result:
# 当前时间戳为： 1626709093.5032222

# 获取当前时间 =  time.struct_time(tm_year=2021, tm_mon=7, tm_mday=19, tm_hour=23, tm_min=38, tm_sec=13, tm_wday=0, tm_yday=200, tm_isdst=0)
# 获取当前时间 =  Mon Jul 19 23:38:13 2021

# 2021-07-19 23:38:13

# 开始时间: 2021-07-19 23:38:13
# 结束时间: 2021-07-19 23:38:18
