import socket
while True:
    client = socket.socket()  # создаем сокет клиента
    hostname = socket.gethostname()  # получаем хост локальной машины
    port = 12345  # устанавливаем порт сервера
    client.connect((hostname, port))  # подключаемся к серверу
    message = input("Input a text: ")  # вводим сообщение
    if "get" in message:
        client.send(message.encode())  # отправляем сообщение серверу
        fx=open("gettedDataFromServer","wb")
        while True:
            data = client.recv(1024)  # получаем данные от сервера
#            print(bytes.decode(data))
            fx.write(data)
            if not data: break
        fx.close()
        client.close()
    elif "send" in message:
        client.send(message.encode())  # отправляем сообщение серверу
        data = client.recv(1024)  # получаем данные с сервера
        print("Server sent: ", data.decode("utf-8"))
        if data.decode("utf-8") == "GET ME FILE":
            filePath = message.split(" ")[1]
            file = open(filePath, "rb")  # открываем файл для отправки
            print("sending data to server")
            line = file.read(1024)
            while (line):
                #            print(line.decode())
                client.send(line)  # отправляем строку клиенту
                print("sStr")
                line = file.read(1024)
            file.close()
        client.close()
    else:
        client.send(message.encode())  # отправляем сообщение серверу
        data = client.recv(1024)  # получаем данные с сервера
        print("Server sent: ", data.decode("utf-8"))
        client.close()  # закрываем подключение