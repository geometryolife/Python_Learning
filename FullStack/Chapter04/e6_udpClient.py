# UDP 实现消息接收与发送 - 客户端
import socket

# 把主机和端口号封装到元组里
HostPort = ('127.0.0.1', 7777)

# 创建 UDP 套接字
udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    user_input = input("请输入要发送给对方的消息: ")
    if user_input == 'quit':
        break
    # 指定地址&端口发送数据，数据必须 encode
    udpCliSock.sendto(user_input.encode('utf8'), HostPort)
    data, addr = udpCliSock.recvfrom(1024)
    msg = data.decode('utf8')
    print("客户端接收消息 {0}".format(msg))

udpCliSock.close()


# >>> Execution Result:
# 请输入要发送给对方的消息: Joe
# 客户端接收消息 Hello Joe
# 请输入要发送给对方的消息: Tom
# 客户端接收消息 Hello Tom
# 请输入要发送给对方的消息: Python
# 客户端接收消息 Hello Python
# 请输入要发送给对方的消息: quit
