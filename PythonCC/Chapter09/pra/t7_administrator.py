print("----------管理员----------")
# 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为
# 完成练习9-3或练习9-5而编写的User类。添加一个名为privilege的
# 属性，用于存储一个由字符串(如"can add post"，"can delete post"、
# "can ban user"等)组成的列表。编写一个名为show_privileges()的方
# 法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。


class User():
    """描述用户信息，并发出个性化问候"""

    def __init__(self, first_name, last_name, hobby, sex):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.hobby = hobby
        self.sex = sex
        self.full_name = self.first_name + " " + self.last_name

    def describe_user(self):
        """打印整洁的描述信息"""
        message = self.full_name.title() + ": " + self.sex
        print(message)

    def greet_user(self):
        """打印个性化问候语"""
        if self.sex == 'male':
            s = 'boy'
        else:
            s = 'girl'
        message = "Do you like " + self.hobby + "?\n"
        message += "Yes, I'm a " + s + ", I like " + self.hobby + ".\n"
        print(message)


class Admin(User):
    """描述管理员"""

    def __init__(self, first_name, last_name, hobby, sex):
        """初始化父类的属性，再初始化管理员特有的属性"""
        super().__init__(first_name, last_name, hobby, sex)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privilege(self):
        """显示管理员的权限"""
        print("The administrator has the following permissions:")
        for privilege in self.privileges:
            print("- " + privilege)


administrator = Admin('joe', 'chen', 'programming', 'male')
administrator.describe_user()
administrator.show_privilege()
