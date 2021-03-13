print("----------以特殊方式跟管理员打招呼----------")
users = ['joe', 'david', 'jenny', 'admin', 'mark']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")
