import socket
import threading

class ChatServer:
    def __init__(self, host='127.0.0.1', port=12345):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(5)
        print(f"Server started on {host}:{port}")
        self.clients = {}

    def broadcast(self, message, sender_socket):
        for client, name in self.clients.items():
            if client != sender_socket:
                try:
                    client.send(message.encode())
                except:
                    client.close()
                    del self.clients[client]

    def handle_client(self, client_socket):
        try:
            name = client_socket.recv(1024).decode()  # Get client's display name
            self.clients[client_socket] = name
            print(f"{name} has joined the chat.")

            while True:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                self.broadcast(message, client_socket)
        except:
            pass
        finally:
            print(f"{self.clients[client_socket]} has left the chat.")
            del self.clients[client_socket]
            client_socket.close()

    def run(self):
        while True:
            client_socket, client_address = self.server.accept()
            print(f"New connection from {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    ChatServer().run()
