# for循环是一种遍历列表的有效方式，但在for循环中不应该修改列表，否则将导
# 致Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可以用
# while循环。

print("----------在列表之间移动元素----------")
# 假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户
# 后，如何将他们移动到另一个已验证用户列表中? 一种方法是使用一个while
# 循环，在验证用户的同时将其从未验证用户列表中提取出来，再将其加入到另
# 一个已验证用户列表中。

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

print(unconfirmed_users)
print(confirmed_users)

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print(unconfirmed_users)
print(confirmed_users)


# ----------在列表之间移动元素----------
# ['alice', 'brian', 'candace']
# []
# Verifying user: Candace
# Verifying user: Brian
# Verifying user: Alice

# The following users have been confirmed:
# Candace
# Brian
# Alice
# []
# ['candace', 'brian', 'alice']
