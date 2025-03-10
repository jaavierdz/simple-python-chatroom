import socket
import threading

class ChatClient:
    def __init__(self):
        host = input("Enter server IP (default 127.0.0.1): ") or '127.0.0.1'
        port = input("Enter server port (default 12345): ")
        port = int(port) if port else 12345
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        print(f"Connected to {host}:{port}")
        
        self.name = input("Enter your display name: ")
        self.client.send(self.name.encode())
        
        threading.Thread(target=self.receive_messages, daemon=True).start()
        self.send_messages()

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                if not message:
                    print("Disconnected from server.")
                    break
                print(message)
            except:
                print("Connection error.")
                break
        self.client.close()

    def send_messages(self):
        while True:
            message = input()
            if message.lower() == 'exit':
                self.client.close()
                print("Disconnected.")
                break
            self.client.send(f"{self.name}: {message}".encode())

if __name__ == "__main__":
    ChatClient()
