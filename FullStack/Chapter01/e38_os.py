# 在 Linux 下查看当前目录下的文件
import os

data = os.popen('ls').read()
print(data)


# >>> Execution Result:
# data
# e10_loop.py
# e11_function.py
# e12_file.py
# e13_bfile.py
# e14_bfile.py
# e15_ifile.py
# e16_count.py
# e17_csvr.py
# e18_csvw.py
# e19_oop.py
# e1_variable.py
# e20_constructor.py
# e21_private.py
# e22_inherit.py
# e23_rewrite.py
# e24_multi.py
# e25_static.py
# e26_special.py
# e27_call.py
# e28_exception.py
# e29_classify.py
# e2_number.py
# e30_traceback.py
# e31_custom.py
# e32_md.py
# e33_pm.py
# e34_CallPm.py
# e35_md.py
# e36_hello.py
# e37_os.py
# e38_os.py
# e3_string.py
# e4_list.py
# e5_fibonacci.py
# e6_tuple.py
# e7_dictionary.py
# e8_set.py
# e9_operator.py
# modulePath
# moduleTest
# __pycache__
