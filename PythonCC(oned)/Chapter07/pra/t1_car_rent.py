#  编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息
car = input("What kind of car do you want to rent? ")

message = "Let me see if I can find you a "

print(message + car.title() + ".")
