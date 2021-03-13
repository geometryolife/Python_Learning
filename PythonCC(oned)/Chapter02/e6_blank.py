# 使用制表符或换行符来添加空白
# 空白: 泛指任何非打印字符，如空格、制表符、换行符
print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 删除空白(末尾), rstrip()方法
# 使用解释器操作
# 暂时性修改
favorite_language = 'python '
favorite_language
favorite_language.rstrip()
favorite_language

print("--------------------")

# 借助变量，永久性修改
favorite_language = 'python '
favorite_language
favorite_language = favorite_language.rstrip()
favorite_language

# 删除空白(开头), lstrip()方法
# 删除空白(两端), strip()方法
favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

print("--------------------")

# 剥除函数最常用于: 在存储用户输入前对其进行清理
