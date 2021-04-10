from collections import OrderedDict

print("----------Python标准库----------")
#  模块collections中的一个类--OrderedDict，能够创建字典并记录其中的键-值
#  对的添加顺序，它兼具列表和字典的主要优点。

#  调用OrderedDict()来创建一个空的有序字典
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
