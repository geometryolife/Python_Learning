#  编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受
#  制造商和型号，还接受任意数量的关键字实参。这样调用这个函数: 提供
#  必不可少的信息，以及两个名称-值对，如颜色和选装配件。
#  打印返回的字典，确认正确地处理了所有的信息
def car_profile(manufacturer, model, **car_info):
    """创建一个字典，其中包含汽车的相关信息"""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model

    for k, v in car_info.items():
        profile[k] = v
    return profile


car = car_profile('subaru', 'outback', color='blue', two_package=True)
print(car)
