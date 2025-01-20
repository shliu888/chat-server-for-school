import socket 
import sys
import time

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_ip=input('What is your IP: ')
server_ip=str(my_ip)
port=8000

server.bind((server_ip,port))
server.listen(0)
print(f'Listening on {server_ip}:{port}')

client_socket,client_address=server.accept()
print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

while True:
    request=client_socket.recv(1024)
    request=request.decode("utf-8")

    if request=='':
        break
    if request!='':
        print(f'Received: {request}')

    myResponse=input('What do you want to send: ')
    if myResponse==' ':
        request=client_socket.recv(1024)
        request=request.decode("utf-8")
        print(f'Most current message from the other user: {request}')
        myResponse1=input('What do you want to send: ')
        client_socket.send(myResponse1.encode('utf-8'))
    if myResponse=='/exit':
        time.sleep(0.5)
        client_socket.send('**CHAT CLOSED BY ANOTHER USER**\n'.encode('utf-8'))
        client_socket.close()
        server.close()
    elif myResponse!=' ' or '/exit':
        client_socket.send(myResponse.encode('utf-8'))
    
