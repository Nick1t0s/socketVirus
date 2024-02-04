def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    b = bytes(result.stdout+result.stderr, "cp8266")
    s = str(b, "cp866")
    return s
import socket,subprocess
client = socket.socket()  # создаем сокет клиента
hostname = socket.gethostname()  # получаем хост локальной машины
port = 12345  # устанавливаем порт сервера
client.connect(('192.168.88.223', port))  # подключаемся к серверу
#while True:
client.send('Tester1'.encode())
#    data=client.recv(1024)
#    data=data.decode()
#    print(data)