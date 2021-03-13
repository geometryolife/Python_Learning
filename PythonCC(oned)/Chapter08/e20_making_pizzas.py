#  Python读取这个文件时，代码行import e19_pizza让Python打开文件
#  e19_pizza.py，并将其中所有函数都复制到这个程序中。
import e19_pizza
print("\n----------导入整个模块----------")

#  编写一条import语句并在其中指定模块名，就可以在程序中使用该
#  模块中的所有函数。
#  如果使用import语句导入名为module_name.py的整个模块，就可以使用:
#  module_name.function_name()来使用模块中的函数。

e19_pizza.make_pizza(16, 'pepperoni')
e19_pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#  ----------将函数存储在模块中----------

#  ----------导入整个模块----------

#  Making a 16-inch pizza with the following toppings:
#  - pepperoni

#  Making a 12-inch pizza with the following toppings:
#  - mushrooms
#  - green peppers
#  - extra cheese
