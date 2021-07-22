import socket

# 创建一个客户端的 socket 对象
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号
port = 12345

# 连接服务，指定主机和端口
clientsocket.connect(('127.0.0.1', port))
print("start Socket Client ...")

# 接收消息，接收小于1024字节的数据
msg = clientsocket.recv(1024).decode('utf-8')
print("client receive message = {0}".format(msg))

# 关闭连接
clientsocket.close()
