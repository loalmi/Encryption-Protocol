import socket
import pickle
from crypt_utils import DiffieHellman, FileCrypter
s = socket.socket()

s.connect(('localhost', 3333)) # Подключаемся к нашему серверу.
s.sendall('Hello! GOOOOD_NIGHTTTT'.encode('utf-8')) # Отправляем фразу.
data = s.recv(1024) #Получаем данные из сокета.

p = 54
g = 53
a = 63  # это можно хранить в txt

diffie_hellman = DiffieHellman(a=a, p=p, g=g)
client_mixed_key = diffie_hellman.mixed_key
private_key = diffie_hellman.generate_key(client_mixed_key)
print(client_mixed_key)
print(private_key)

s.send(pickle.dumps((p, g, client_mixed_key)))
s.close()

s = socket.socket()
s.connect(('localhost', 3333))
crypter = FileCrypter(private_key)
result = crypter.encryption("ТЕСТОВАЯ СТРОКАААА")
print(result)
s.send(pickle.dumps(result))

result = crypter.encryption(result)
print(result)

s.close()
print(data)