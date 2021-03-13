#  编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所
#  属的国家。这个函数应打印一个简单的句子，如 Reykjavik is in Iceland。
#  给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中
#  至少有一座城市不属于默认国家。


def describe_city(city, nation='China'):
    """描述城市信息"""
    print(city + " is in " + nation + ".")


describe_city('ShangHai')
describe_city('BeiJing')
describe_city(city='ShenZhen')
describe_city('Reykjavik', 'Iceland')
describe_city(city='New York', nation='US')
