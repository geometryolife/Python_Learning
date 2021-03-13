import e19_pizza as p

print("\n----------使用as给模块指定别名----------")
#  不仅能使代码更简洁，还可以让你不再关注模块名，而专注于描述性的函数名。
#  这些函数名明确地指出了函数的功能，对理解代码而言，它们比模块名更重要。

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
