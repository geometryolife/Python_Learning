from e19_pizza import make_pizza

print("\n----------导入特定的函数----------")

#  语法:
#  使用这种语法，显式地导入了函数，调用函数时就无需使用句点
#  from module_name import function_name
#  根据需要从模块中导入任意数量的函数
#  from module_name import function_0, function_1, function_2

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
