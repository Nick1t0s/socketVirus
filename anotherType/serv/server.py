class cl:
    def __init__(self,ip,name,p):
        self.ip=ip
        self.port=p
        self.name=name
x={}
import socket

server = socket.socket()  # создаем объект сокета сервера
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 12345  # устанавливаем порт сервера
server.bind(('192.168.1.13', port))  # привязываем сокет сервера к хосту и порту
server.listen(5)  # начинаем прослушиваение входящих подключений
print("Server running")
while True:
    con, c2 = server.accept()  # принимаем клиента
    data = con.recv(1024)  # получаем данные от клиента
    message = data.decode()  # преобразуем байты в строку
    print(con.laddr)
    print(message,con,c2)