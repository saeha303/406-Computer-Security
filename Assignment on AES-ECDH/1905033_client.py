# alice
import socket
import _1905033_utils_elliptic
import _1905033_aes

s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
intended_len = input('Intended message length: ')
intended_len = int(intended_len, 10)
# alice to bob
p, ka, a, b, x1, y1 = _1905033_utils_elliptic.for_alice(intended_len)
# calculate public key
Ax, Ay = _1905033_utils_elliptic.calculateAB(ka, a, b, p, x1, y1)
data_to_send = str(a) + ' ' + str(b) + ' ' + str(p) + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(Ax) + ' ' + str(Ay)
s.send(data_to_send.encode())
# print(data_to_send)
# receive from bob
public_key = s.recv(1024).decode()
split_result = public_key.split()
Bx = int(split_result[0], 10)
By = int(split_result[1], 10)
# send

# shared secret key
Rx, Ry = _1905033_utils_elliptic.calculateAB(ka, a, b, p, Bx, By)
print('Plain text:')
plain = input()
key = bin(Rx)[2:].zfill(128)
key = ''.join([chr(int(key[i:i + 8], 2)) for i in range(0, 128, 8)])
# print('key: ',key)
# confirm
s.send('Alice says: I am ready to send'.encode())
confirmation = s.recv(1024).decode()
print(confirmation)
cipher = _1905033_aes.encryption(key, plain)
s.send(cipher.encode())
s.close()
