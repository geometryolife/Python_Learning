print("----------有意义的变量名----------")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

#  注意: 遍历字典时，键-值对的返回顺序也与存储顺序不同

print("\n----------遍历键-值对items()----------")
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite_language is " + language.title() + ".")

print("\n----------遍历键keys()----------")
#  方法keys()返回一个键列表
for name in favorite_languages.keys():
    print(name.title())

print("\n----------默认遍历所有的键----------")
#  显式使用keys()可以让代码更容易理解
for name in favorite_languages:
    print(name.title())

print("\n----------使用当前键来访问与之相关联的值----------")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

print("\n----------确定某个人是否接受了调查----------")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n----------按顺序遍历字典中的所有键----------")
#  获取字典的元素时，获取顺序是不可预测的
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\n----------遍历字典中的所有值values()----------")
#  方法values()返回一个值列表
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n----------集合set()----------")
#  集合类似于列表，但每个元素都必须独一无二，用于剔除重复项
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
