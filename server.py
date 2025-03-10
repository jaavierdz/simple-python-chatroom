import socket
import threading

class ChatClient:
    def __init__(self):
        host = input("Enter server IP (default 127.0.0.1): ") or '127.0.0.1'
        port = input("Enter server port (default 12345): ")
        port = int(port) if port else 12345
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        threading.Thread(target=self.receive_messages, daemon=True).start()

        while True:
            message = input()
            if message.lower() == 'exit':
                self.client.close()
                break
            self.client.send(message.encode())

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                if not message:
                    break
                print("\n" + message)
            except:
                break

if __name__ == "__main__":
    ChatClient()
