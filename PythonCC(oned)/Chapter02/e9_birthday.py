# 类型错误
#  age = 23
#  message = "Happy " + age + "rd Birthday!"
#  print(message)

#  Traceback (most recent call last):
#  File "e9_birthday.py", line 2, in <module>
#  message = "Happy " + age + "rd Birthday!"
#  TypeError: can only concatenate str (not "int") to str

print("--------------------")

# 使用函数str()避免类型错误
age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)
