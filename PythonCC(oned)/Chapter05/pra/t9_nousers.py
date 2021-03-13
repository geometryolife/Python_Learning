print("----------处理没有用户的情形----------")
users = ['joe', 'david', 'jenny', 'admin', 'mark']

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")

#  删除表中的所有用户
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again.")
else:
    print("\nWe need to find some users!")

print("\n----------改进版----------")
