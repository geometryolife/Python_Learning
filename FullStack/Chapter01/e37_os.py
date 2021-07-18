# Python 中可以使用 os 模块来处理文件和目录。os 模块不受平台限制，可以执行
# 操作系统命令。
# os.popen() 方法用于从一个命令打开一个管道，在 Linux、Windows 中有效。

# 在 Linux 下查询系统 I/O 状况信息。
# Linux 系统中通过 iostat 命令查看系统的 I/O 状态信息，从而确定 I/O 性能
# 是否存在"瓶颈"。常用于服务端性能分析。
import os
import time

# 每5秒执行一次 iostat 命令
while True:
    # 获得执行命令的输出
    data = os.popen('iostat').read()
    print(data)
    time.sleep(5)


# >>> Execution Result:
# Linux 5.4.0-72-generic (VM-12-14-ubuntu)        07/18/2021      _x86_64_        (1 CPU)

# avg-cpu:  %user   %nice %system %iowait  %steal   %idle
    # 2.48    0.02    0.93    0.10    0.00   96.47

# Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd
# scd0              0.00         0.02         0.00         0.00       8420          0          0
# vda               3.79         3.78        34.92         0.00    1411051   13045676          0
