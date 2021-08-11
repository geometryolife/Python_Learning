# UDP 实现消息接收与发送 - 服务端
import socket

# 把主机和端口号封装到元组里
HostPort = ('127.0.0.1', 7777)

# 创建 UDP 套接字
udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务器端绑定端口
udpSerSock.bind(HostPort)

while True:
    # 接收数据和客户端的地址&端口
    data, addr = udpSerSock.recvfrom(1024)
    # 打印数据
    print("服务器接收消息: ", data.decode('utf8'))
    sendMsg = "Hello {0}".format(data.decode('utf8'))
    udpSerSock.sendto(sendMsg.encode('utf8'), addr)

udpSerSock.close()


# >>> Execution Result:
# 服务器接收消息:  Joe
# 服务器接收消息:  Tom
# 服务器接收消息:  Python
