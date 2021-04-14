import unittest
from e6_name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    # 添加新测试
    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()


# 测试未通过时，不要修改测试，而应修复导致测试不能通过的代码

# 准确的命名测试方式能够快速清楚地指出它测试的是被测函数的哪个行为。
# 1.在TestCase类中使用很长的方法名是可以的；
# 2.这些方法的名称必须是描述性的，快速明白测试未通过时的输出；
# 3.这些方法由Python自动调用，不必编写调用代码。


# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# OK
