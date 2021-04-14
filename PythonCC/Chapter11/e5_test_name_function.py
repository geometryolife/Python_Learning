import unittest
from e4_name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()

# 字母E指出测试用例中有一个单元测试导致了错误。
# E
# 测试用例包含众多单元测试时，知道哪个测试未通过至关重要。
# ======================================================================
# ERROR: test_first_last_name (__main__.NameTestCase)
# 能够正确地处理像Janis Joplin这样的姓名吗?
# 输出一个标准的traceback
# ----------------------------------------------------------------------
# Traceback (most recent call last):
# File "e5_test_name_function.py", line 10, in test_first_last_name
# formatted_name = get_formatted_name('janis', 'joplin')
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'

# ----------------------------------------------------------------------
# 运行了一个单元测试
# Ran 1 test in 0.011s

# 指出整个测试用例都未通过，运行该测试用例时发生了一个错误
# FAILED (errors=1)
