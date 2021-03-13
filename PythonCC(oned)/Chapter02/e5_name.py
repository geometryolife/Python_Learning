# 使用方法修改字符串的大小写
name = "ada lovelace"
print(name.title())

print("--------------------")

# 很多时候无法靠用户来提供正确的大小写，因此需要将字符串先转化为小写，
# 再存储他们，当需要显示这些信息时，再将其转换为最合适的大小写。
name = "ADA LOVELACE"
print(name.upper())
print(name.lower())

print("--------------------")

# 思考: 将Ada、ADA、ada视为同一个值
t1 = "Ada"
t2 = "ADA"
t3 = "ada"
print(t1)
print(t2)
print(t3)

t1.lower()
print(t1.title())

t2.lower()
print(t2.title())

t3.lower()
print(t3.title())

print("--------------------")

# 合并(拼接)字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

# 拼接后存入变量，再使用
message = "Hello, " + full_name.title() + "!"
print(message)
