import time
from Admin import Admin
import pickle
from ATM import ATM
import os


def main():
    # 界面对象
    admin = Admin()

    # 管理员开机
    admin.AdminView()
    if admin.Check():
        return -1

    # 存储信息的文件是否存在
    if os.path.exists("userinfo.txt"):
        filepath = "userinfo.txt"
    else:
        open("userinfo.txt", "wb")
        filepath = "userinfo.txt"

    # 如果存储信息的文件非空
    if os.path.getsize(filepath):
        f = open(filepath, "rb")
        allusers = pickle.load(f)
    else:
        allusers = {}

    # 在登陆时，打印所有银行储户
    # print((allusers))

    # 提款机对象
    atm = ATM(allusers)

    while True:
        admin.FunctionView()
        # 等待用户操作
        option = input("请输入您的操作：")
        if option == '1':
            # 开户
            atm.CreatUser()
        elif option == '2':
            # 查询
            atm.searchUserInfo()
        elif option == '3':
            # 取款
            atm.getMoney()
        elif option == '4':
            # 存款
            atm.saveMoney()
        elif option == '5':
            # 转账
            atm.transferMoney()
        elif option == '6':
            # 改密码
            atm.changePasswd()
        elif option == '7':
            # 锁定
            atm.lockUser()
        elif option == '8':
            # 解锁
            atm.unlockUser()
        elif option == '9':
            # 补卡
            atm.newCard()
        elif option == '10':
            # 销户
            atm.killUser()
        elif option == '0':
            # 退出
            if not admin.Check():
                # 将当前系统中的用户信息保存到文件中
                f = open(filepath, "wb")
                # pickle 序列化后的数据,可读性差，提高安全性
                pickle.dump(atm.allUsers, f)
                f.close()
                return -1

        time.sleep(1)


if __name__ == "__main__":
    main()
