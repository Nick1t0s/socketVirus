def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    b = bytes(result.stdout+result.stderr, "cp1251")
    s = str(b, "cp866")
    return s
import socket
import subprocess
server = socket.socket()  # создаем объект сокета сервера
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 12345  # устанавливаем порт сервера
server.bind((hostname, port))  # привязываем сокет сервера к хосту и порту
server.listen(5)  # начинаем прослушиваение входящих подключений

print("Server running")
while True:
    con, _ = server.accept()  # принимаем клиента
    data = con.recv(1024)  # получаем данные от клиента
    message = data.decode()  # преобразуем байты в строку
    print(f"Client sent: {message}")
    if "get" in message:
        print('sfsgfdgdfgfgfdgfggfdfgffgdfgfdfgg')
        filePath=message.split(" ")[1]
        file = open(filePath, "rb")  # открываем файл для отправки
        print(f"sending data to client {filePath}")
        # считываем данные из файла блоками по 1024 байт и отправляем клиенту
        line = file.read(1024)
        while (line):
#            print(line.decode())
            con.send(line)  # отправляем строку клиенту
            line = file.read(1024)

        file.close()  # закрываем файл
        con.close()
    elif "send" in message:
        pathToGet=message.split(" ")[1]
        print(pathToGet)
        con.send("GET ME FILE".encode("utf-8"))
        fx = open(pathToGet, "wb")
        while True:
            data = con.recv(1024)  # получаем данные от сервера
            #            print(bytes.decode(data))
            fx.write(data)
            print("gfdfff")
            if not data: break
        fx.close()
        con.close()
    else:
        x=run_command(message)
        print(f"result {x}")
    #    message = x[::-1]  # инвертируем строку
        con.send(x.encode("utf-8"))  # отправляем сообщение клиенту
        con.close()