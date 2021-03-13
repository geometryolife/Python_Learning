print("----------使用breal退出循环----------")
#  要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的
#  结果如何，可以使用break语句

#  让用户指出他到过哪些地方的程序。在这个程序中，我们可以在用户输入
#  'quit'后使用break语句立即退出while循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

#  注意: 在任何Python循环中都可使用break语句。
#  例如，可使用break语句来退出遍历列表或字典的for循环
