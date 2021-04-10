print("----------编写清晰的程序----------")
name = input("Please enter your name: ")
print("Hello, " + name + "!")

print("\n----------字符串末尾附加一个字符串----------")
prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

print("\n----------使用int()来获取数值输入----------")
age = input("How old are you? ")
print(age)
#  age >= 18
#  使用函数int()，解决无法将字符串和整数进行比较的问题
age = int(age)
print(age >= 18)
