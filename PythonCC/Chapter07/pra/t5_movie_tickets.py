print("----------电影票----------")

# 有家电影院根据观众的年龄收取不同的票价: 不到3岁的观众免费；
# 3~12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，
# 在其中询问用户的年龄，并指出其票价。
prompt = input("How old are you? ")

age = int(prompt)
while True:
    if age < 3:
        print("Younger than 3 years old, no tickets are require.")
        continue
    elif age <= 12:
        print("You need to pay $10.")
        break
    elif age > 12:
        print("You need to pay $15.")
        break
    elif age < 0 and age > 100:
        print("Please enter a valid age!")
        break
