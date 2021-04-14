print("----------用户----------")
#  创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常
#  会存储的几个属性。在类User中定义一个名为describe_user()的方法，它打印用户
#  信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。


class User():
    """描述用户信息，并发出个性化问候"""

    def __init__(self, first_name, last_name, hobby, sex):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.hobby = hobby
        self.sex = sex
        self.full_name = self.first_name + ' ' + self.last_name

    def describe_user(self):
        """打印整洁的描述信息"""
        message = self.full_name.title() + ": " + self.sex
        print(message)

    def greet_user(self):
        """打印个性化问候语"""
        if self.sex == "male":
            s = "boy"
        else:
            s = "girl"
        message = "Do you like " + self.hobby + "?\n"
        message += "Yes, I'm a " + s + ", I like " + self.hobby + ".\n"
        print(message)


user1 = User('joe', 'chen', 'programming', 'male')
user1.describe_user()
user1.greet_user()

user2 = User('david', 'zhang', 'playing basketball', 'male')
user2.describe_user()
user2.greet_user()

user3 = User('Lucy', 'jonse', 'singing', 'female')
user3.describe_user()
user3.greet_user()
