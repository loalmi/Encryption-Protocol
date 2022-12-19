from crypt_utils import DiffieHellman, FileCrypter
import socket
sock = socket.socket()
sock.bind(('', 3333)) # Привязываем серверный сокет к localhost и 3030 порту.
sock.listen(1) # Начинаем прослушивать входящие соединения
conn, addr = sock.accept() # Метод который принимает входящее соединение.

crypter = None
while True: # Создаем вечный цикл.
	data = conn.recv(1024) # Получаем данные из сокета.
	if type(data) == tuple:
		p, g, A = data

		diffie_hellman = DiffieHellman(a=A, p=p, g=g)
		server_mixed_key = diffie_hellman.mixed_key
		private_key = diffie_hellman.generate_key(server_mixed_key)
		crypter = FileCrypter(private_key)
		print(server_mixed_key)
		print(private_key)

	elif type(data) == str:
		result = crypter.encryption(data)
		print(result)

	else:
		raise ValueError(f"Был принят некорректный тип data: {type(data)}")
	conn.sendall(data) # Отправляем данные в сокет.
	print(data.decode('utf-8')) # Выводим информацию на печать.
conn.close()