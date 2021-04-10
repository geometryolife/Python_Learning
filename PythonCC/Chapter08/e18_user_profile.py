print("----------使用任意数量的关键字实参----------")
#  有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么
#  样的信息。此时，可以将函数编写成能够接受任意数量的键-值对--调用
#  语句提供了多少就接受多少。

#  形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并
#  将收到的所有名称-值对都封装到这个字典中。

#  创建用户简介: 你将收到有关用户的信息，但不确定会是什么样的信息。


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)


#  ----------使用任意数量的关键字实参----------
#  {'first_name': 'albert', 'last_name': 'einstein',
#  'location': 'princeton', 'field': 'physics'}

#  总结:
#  调用这个函数时，不管额外提供了多少个键-值对，它都能正确处理。
#  编写函数时，可以混合使用位置实参、关键字实参和任意数量的实参。
