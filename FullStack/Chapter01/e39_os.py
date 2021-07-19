# os.listdir() 方法用于返回指定的文件夹包含的文件和目录的名称列表。
import os

# os.listdir() 如果不指定 path 参数，则列出执行脚本当前目录下的
# 文件和目录的列表。
print(os.listdir(), '\n')

# 输出 Python_Learning 目录下的所有文件和目录的名称列表
dirs = os.listdir('../../../Python_Learning')
print(dirs)


# >>> Execution Result:
# ['e20_constructor.py', 'e5_fibonacci.py', 'e33_pm.py', 'e30_traceback.py',
# 'e21_private.py', 'e2_number.py', 'e13_bfile.py', 'e14_bfile.py', 'e9_operator.py',
# 'e37_os.py', 'e22_inherit.py', 'e18_csvw.py', 'e11_function.py', 'e29_classify.py',
# 'e31_custom.py', 'e28_exception.py', 'e38_os.py', 'e24_multi.py', 'data', 'e10_loop.py',
# 'e17_csvr.py', 'e34_CallPm.py', 'e15_ifile.py', 'modulePath', '__pycache__', 'e32_md.py',
# 'e8_set.py', 'e4_list.py', 'e25_static.py', 'e16_count.py', 'e39_os.py',
# 'moduleTest', 'e12_file.py', 'e7_dictionary.py', 'e19_oop.py', 'e1_variable.py',
# 'e6_tuple.py', 'e27_call.py', 'e35_md.py', 'e36_hello.py', 'e23_rewrite.py',
# 'e3_string.py', 'e26_special.py']

# ['Action', '.gitignore', 'PythonCC', '.git', 'DataStructure', 'FullStack', 'README.md', '.vim']
