def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    b = bytes(result.stdout+result.stderr, "cp1251")
    s = str(b, "cp866")
    return s
import socket
client = socket.socket()  # создаем сокет клиента
hostname = socket.gethostname()  # получаем хост локальной машины
port = 12345  # устанавливаем порт сервера
client.connect(('192.168.1.13', port))  # подключаемся к серверу
while True:
    client.send('Tester'.encode())
    data=client.recv(1024)
    data=data.decode()
    print(data)