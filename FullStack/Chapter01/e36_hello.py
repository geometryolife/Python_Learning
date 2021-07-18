def sayHello():
    print("Hello Python!")


# 程序的入口，与 C 语言的 main() 函数相当
if __name__ == '__main__':
    print("This is main of module 'hello.py'")
    sayHello()


# >>> Execution Result:
# This is main of module 'hello.py'
# Hello Python!

# 当作模块运行:
# >>> import e36_hello
# >>> e36_hello.sayHello()
# Hello Python!
# >>> e36_hello.__name__
# 'e36_hello'

# 解释:
# 当 e36_hello.py 脚本当作模块导入时，其中的 "if __name__ == '__main__':" 后面
# 的代码块不会被执行。如果作为模块引入，那么 e36_hello.__name__ 等于 "hello"，
# 即 __name__ 的值是模块名称。

# 作用:
# 在 Python 中，当一个 module 作为整体被执行时，module.__name__ 的值
# 是 "__main__"，而当一个 module 被其他 module 引用时，其本身并不需要
# 一个可执行的入口 main。

# 意义:
# 在定义完一个类后，对类的引用放在 "if __name__ = '__main__':" 语句后，
# 方便代码的调试。
