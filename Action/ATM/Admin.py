import time


class Admin(object):
    # 管理员账号与密码，类属性，作为全局变量
    admin = '1'
    passwd = '1'

    # 管理员界面
    def AdminView(self):
        print("**********************************************")
        print("*                                            *")
        print("*                                            *")
        print("*               欢迎登录ACE银行              *")
        print("*                                            *")
        print("*                                            *")
        print("**********************************************")

    # 功能界面
    def FunctionView(self):
        print("**********************************************")
        print("*           开户（1）     查询（2）          *")
        print("*           取款（3）     存款（4）          *")
        print("*           转账（5）     改密码（6)         *")
        print("*           锁定（7）     解锁（8）          *")
        print("*           补卡（9）     销户（10）         *")
        print("*                   退出（0）                *")
        print("**********************************************")

    # 管理员验证
    def Check(self):
        inputAdmin = input("请输入管理员账户: ")
        if self.admin != inputAdmin:
            print("账号输入错误！")
            return -1
        inputPasswd = input("请输入管理员密码: ")
        if self.passwd != inputPasswd:
            print("密码输入错误！")
            return -1
        # 能执行到这里说明账号密码输入正确
        print("操作成功,请稍后...")
        time.sleep(1)
        return 0
