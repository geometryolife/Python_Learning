# 城市和国家
# 编写一个函数，它接受两个形参: 一个城市名和一个国家名。这个函数返回一个
# 格式为City，Country的字符串，如Santiage，Chile。将这个函数存储在一个名
# 为city_functions.py的模块中。
# 创建一个名为test_cites.py的程序，对刚编写的函数进行测试(别忘了，你需要导
# 入模块unittest以及要测试的函数)。编写一个名为test_city_country()的方法，
# 核实使用类似于'santiage'和'chile'这样的值来调用前述函数时，得到的字符串
# 是正确的。运行test_cites.py，确认测试test_city_country()通过了。


import unittest
from t1_city_function import city_country


class CitiesTestCase(unittest.TestCase):
    """测试city_function.py"""

    def test_city_country(self):
        """能够正确地处理像Santiage,Chile这样的城市描述吗?"""
        city_country_str = city_country('santiage', 'chile')
        self.assertEqual(city_country_str, 'Santiage, Chile')


unittest.main()
