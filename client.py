import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345

client.connect((host,port))

while True :
    msg= input("Client : ")
    client.send(msg.encode())
    if msg.lower()=="exit":
        break

    server_msg = client.recv(1024).decode()
    print("Server :",server_msg)
    if server_msg=="exit":
        break

client.close()