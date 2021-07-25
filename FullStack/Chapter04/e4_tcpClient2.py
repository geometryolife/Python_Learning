# TCP 聊天室
import socket

# 创建一个客户端的 socket 对象
tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置端口号
port = 12345

# 连接服务，指定主机和端口
tcpCliSock.connect(('127.0.0.1', port))
print("Start Socket client ...")

while True:
    data = input("请在客户端输入发送的内容: ")

    if not data:
        break
    tcpCliSock.send(data.encode('utf8'))
    client_data = tcpCliSock.recv(1024)
    if not client_data:
        break

    print("客户端接收的消息为: ", client_data.decode('utf8'))

# 关闭连接
tcpCliSock.close()


# >>> Execution Result:
# Start Socket client ...
# 请在客户端输入发送的内容: Hello Joe.
# 客户端接收的消息为:  服务器当前时间 = Sun Jul 25 16:28:20 2021
# 请在客户端输入发送的内容: 东京奥运会，中国加油!
# 客户端接收的消息为:  服务器当前时间 = Sun Jul 25 16:28:39 2021
# 请在客户端输入发送的内容: ZGNB!!!
# 客户端接收的消息为:  服务器当前时间 = Sun Jul 25 16:28:51 2021
# 请在客户端输入发送的内容:
# 客户端接收的消息为:  服务器当前时间 = Sun Jul 25 16:28:55 2021
# 请在客户端输入发送的内容: quit
