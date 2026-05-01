# Ex.No:1b – Study of Client Server Chat Applications

---

## Aim
To perform a study on Client Server Chat Applications.

---

## Introduction
Client-server chat applications are networked software systems that enable real-time communication between users over a network. In this model, the server manages connections and communication, while the client sends and receives messages through the server.

---

## 1. Client-Server Model
- **Server:** A central component that listens for incoming client connections, manages communication channels, and may handle authentication and message routing.  
- **Client:** A user/device that connects to the server, usually with a username, to participate in the chat and exchange messages.  

---

## 2. Communication Protocols
- **TCP (Transmission Control Protocol):** Reliable, connection-oriented communication; ensures ordered and error-free message delivery.  
- **UDP (User Datagram Protocol):** Connectionless and faster, but messages may be lost or arrive out of order.  

---

## 3. Socket Programming
- Sockets act as communication endpoints for both client and server.  
- Common socket functions include `socket()`, `bind()`, `listen()`, `accept()`, `connect()`, `send()`, and `recv()`.  

---

## 4. User Authentication
Chat applications often use authentication methods such as username-password login or token-based access to improve security and privacy.  

---

## 5. Message Routing
The server is responsible for routing messages from one client to another and ensuring that each message reaches the intended recipient. It may maintain a list of connected users and their sockets.  

---

## 6. Server-Side Components
- Socket handling  
- User management  
- Message routing  

---

## 7. Considerations in Development
- Concurrency and multithreading  
- Security  
- Scalability  
- Persistence  
- Notification systems  

---

## Program

The sample implementation uses Python socket programming with a server on `127.0.0.1:12345` and a client that connects to it. The server receives messages in a loop and sends replies until either side types `exit`.

---

### Server
```python
import socket

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

# Bind and listen
server.bind((host, port))
server.listen(1)
print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    # Receive message from client
    client_msg = conn.recv(1024).decode()
    print("Client:", client_msg)
    if client_msg.lower() == "exit":
        break

    # Send message to client
    msg = input("Server: ")
    conn.send(msg.encode())
    if msg.lower() == "exit":
        break

conn.close()
server.close()
```

### Client
```python
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

client.connect((host,port))

while True:
    msg= input("Client:")
    client.send(msg.encode())
    if msg.lower()=="exit":
        break

    server_msg=client.recv(1024).decode()
    print("Server:",server_msg)
    if server_msg.lower()=="exist":
        break

client.close()
```

## Output

### Server
![alt text](<Screenshot 2026-05-01 140459.jpeg>)

### Client
![alt text](<Screenshot 2026-05-01 140534.png>)

## Result:

Thus the study on Client Server Chat Applications has been performed successfully.
