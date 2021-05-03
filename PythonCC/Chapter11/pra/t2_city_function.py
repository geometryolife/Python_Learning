# 修改前面的函数，使其包含第三个必不可少的形参population，并返回一个格式为
# City，Country - population xxx 的字符串，如Santiage，Chile - population
# 5000000。运行test_cities.py，确认测试test_city_country()未通过。
# 修改上述函数，将形参population设置为可选的。再次运行test_cities.py，确认
# 测试test_city_country()又通过了。
# 再编写一个名为test_city_country_population()的测试，核实可以使用类似于
# 'santiage'、'chile'和'population=5000000'这样的值来调用这个函数。再次运
# 行test_cities.py，确认测试test_city_country_population()通过了。


def city_country(city, country, population=''):
    """返回描述城市的整洁字符串"""
    if population:
        msg = city.title() + ", " + country.title() + " - population " + \
            str(population)
    else:
        msg = city.title() + ", " + country.title()
    return msg
