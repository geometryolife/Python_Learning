from e19_pizza import make_pizza as mp

print("\n----------使用as给函数指定别名----------")
#  如果要导入的函数的名称与程序中现有的名称冲突，或者名称太长，
#  可指定简短而独一无二的别名--函数的另一个名称，类似于外号。
#  使用关键字as

#  语法:
#  from module_name import function_name as fn

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
