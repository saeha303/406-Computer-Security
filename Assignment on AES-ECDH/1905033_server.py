# bob
import socket
import _1905033_aes
import _1905033_utils_elliptic
s = socket.socket()
# print ("Socket successfully created")
port = 12345
s.bind(('', port))
# print ("socket binded to %s" %(port))
s.listen(5)
# print ("socket is listening")
while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    # receive from alice
    data_received = c.recv(1024).decode()
    split_result = data_received.split()
    a=int(split_result[0],10)
    b=int(split_result[1],10)
    p=int(split_result[2],10)
    x1=int(split_result[3],10)
    y1=int(split_result[4],10)
    Ax=int(split_result[5],10)
    Ay=int(split_result[6],10)
    # print(data_received)
    kb=_1905033_utils_elliptic.for_bob(p)
    # calculate public key
    Bx,By=_1905033_utils_elliptic.calculateAB(kb,a,b,p,x1,y1)
    print('Received a, b, p, G, Ka*G mod p from Alice')
    # send to alice
    data_to_send = str(Bx)+' '+str(By)
    c.send(data_to_send.encode())

    #shared secret key
    Rx, Ry = _1905033_utils_elliptic.calculateAB(kb, a, b, p, Ax, Ay)
    key = bin(Rx)[2:].zfill(128)
    key = ''.join([chr(int(key[i:i + 8], 2)) for i in range(0, 128, 8)])
    # print('key: ',key)
    #confirm

    confirmation = c.recv(1024).decode()
    c.send('Bob says: I am ready to receive'.encode())
    print(confirmation)
    # print('key: ', key)
    cipher=c.recv(1024).decode()
    plain=_1905033_aes.decryption(key,cipher)
    c.close()
    break
