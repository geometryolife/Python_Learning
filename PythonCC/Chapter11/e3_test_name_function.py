import unittest
from e1_name_function import get_formatted_name


print("----------单元测试和测试用例----------")
# Python标准库中的模块unittest提供了代码测试工具。

# 1.单元测试用于核实函数的某个方面没有问题；
# 2.测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的
# 行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，
# 包含针对所有这些情形的测试。
# 3.全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。

# 大型项目要实现全覆盖可能很难，通常最初只针对代码的重要行为编写测试
# 即可，等项目被广泛使用时再考虑全覆盖。

print("\n----------可通过的测试----------")
# 创建测试用例的语法需要一段时间才能习惯，但测试用例创建后，再添加针对
# 函数的单元测试就很简单了。

# 要为函数编写测试用例，先导入模块unittest以及要测试的函数，再创建一
# 个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面
# 进行测试。


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # 断言方法，unittest中最有用的功能之一，assertEqual()将
        # formatted_name与字符串'Janis Joplin'比较
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()

# 编写测试类名时，名字最好与要测试的函数相关，并包含字样Test。
# 这个类必须继承unittest.TestCase类，当运行程序时，所有以test_打头
# 的方法都将自动运行。


# 句点表明有一个测试通过了
# .
# ----------------------------------------------------------------------
# 指出Python运行了一个测试，消耗时间为多少
# Ran 1 test in 0.012s

# 最后的OK表明该测试用例中的所有单元测试都通过了
# OK
