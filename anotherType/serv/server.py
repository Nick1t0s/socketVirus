def applyUsers():
    global x
    while True:
        con, c2 = server.accept()  # принимаем клиента
        data = con.recv(1024)  # получаем данные от клиента
        message = data.decode()  # преобразуем байты в строку
        x[message] = con
        print(f"Warring new client with name {message}")
        logging.info(f"Ура новый клиент с имем {message}")

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
def getClient():
    global tr
    tr = ""
    while not tr in x:
        c = 0
        for i in x:
            print(f"{c} {i}")
            c += 1
        tr=input("Select target:")
        print()
def getData():
    global x
    x[tr].send(command.encode())  # отправляем сообщение серверу
    fx = open("gettedDataFromServer", "wb")
    while True:
        jdata = x[tr].recv(1024)  # получаем данные от сервера
        #            print(bytes.decode(data))
        fx.write(jdata)
        print(jdata)
        if not jdata:
            print("dfsdffsd")
            break
    fx.close()
import threading
x={}
import socket
import pickle
import logging
target=None

server = socket.socket()  # создаем объект сокета сервера
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 12346  # устанавливаем порт сервера
server.bind(('192.168.88.223', port))  # привязываем сокет сервера к хосту и порту
server.listen(5)  # начинаем прослушиваение входящих подключений
print("Server running")
#users=getUsersFromFile()
chUs=threading.Thread(target=applyUsers)
chUs.start()
tr=""
getClient()
while True:
    command=input("Write your command: ")
    if "exit" in command:
        getClient()
        command = input("Write your command: ")
    elif "get" in command:
        x[tr].send(command.encode())  # отправляем сообщение серверу
        fx = open("gettedDataFromServer", "wb")
        while True:
            data = x[tr].recv(1024)  # получаем данные от сервера
            #            print(bytes.decode(data))
            fx.write(data)
            if not data: break
        fx.close()
        print("done")
        command = input("Write your command: ")
    else:
        x[tr].send(command.encode())
        res=x[tr].recv(1024).decode()
        print(res)