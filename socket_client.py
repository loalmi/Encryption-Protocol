import socket
s = socket.socket()

s.connect(('localhost', 3333)) # Подключаемся к нашему серверу.
s.sendall('Hello! GOOOOD_NIGHTTTT'.encode('utf-8')) # Отправляем фразу.
data = s.recv(1024) #Получаем данные из сокета.
s.close()
print(data)