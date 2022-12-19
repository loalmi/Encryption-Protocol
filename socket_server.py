
import socket
sock = socket.socket()
sock.bind(('', 3333)) # Привязываем серверный сокет к localhost и 3030 порту.
sock.listen(1) # Начинаем прослушивать входящие соединения
conn, addr = sock.accept() # Метод который принимает входящее соединение.

while True: # Создаем вечный цикл.
	data = conn.recv(1024) # Получаем данные из сокета.
	if not data:
		break
	conn.sendall(data) # Отправляем данные в сокет.
	print(data.decode('utf-8')) # Выводим информацию на печать.
conn.close()