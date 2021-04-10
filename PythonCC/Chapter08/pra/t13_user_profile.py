#  复制前面的程序user_profile.py，在其中调用build_profile()来创建有关
#  你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。

def user_profile(first, last, **infos):
    """整洁打印名字及相关描述信息"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for k, v in infos.items():
        profile[k] = v
    return profile


myinfo = user_profile('Joe', 'Chen', lovesong='Lover', city='ShenZhen', age=24)
print(myinfo)

print("\n----------改进----------")


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['name'] = first.title() + ' ' + last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('joe', 'chen',
                             location='ShenZhen',
                             position='student')
print(user_profile)
