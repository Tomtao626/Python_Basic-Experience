#导入socket
import socket
#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#指向一个网站
s.connect(('www.sina.com',80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
    data = b''.join(buffer)
# 关闭连接:
s.close()
header,html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)


