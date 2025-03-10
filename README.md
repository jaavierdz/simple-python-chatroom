# Simple Python Chatroom (Server and Client)

This project implements a simple console-based chatroom using Python sockets and threading. It consists of a server that handles multiple clients and a client that connects to the server.

## Features
- Multiple clients can connect to the chatroom simultaneously.
- Clients can send messages to the server, which broadcasts them to all connected clients.
- Clients can exit by typing `exit`.
- The client prompts the user to enter the server IP and port on startup.

## Requirements
- Python 3.x

## How to Run

### Running the Server
1. Open a terminal and navigate to the project directory.
2. Run the server script:
   ```sh
   python server.py
   ```
   The server will start listening for connections on `127.0.0.1:12345`.

### Running a Client
1. Open a new terminal window.
2. Run the client script:
   ```sh
   python client.py
   ```
3. Enter the server's IP and port when prompted.
4. Start typing messages to chat with other connected clients.
5. Type `exit` to leave the chat.

## File Structure
- `server.py` - Contains the chatroom server implementation.
- `client.py` - Contains the chatroom client implementation.

## How It Works
- The **server** listens for incoming connections and starts a new thread for each client.
- The **client** connects to the server and listens for messages while allowing the user to type and send messages.
- The **server broadcasts** received messages to all connected clients.

## Example Usage
```
Client 1: Hello everyone!
Client 2: Hi!
Client 3: Hey there!
```

## Future Improvements
- Implement user authentication.
- Add a GUI for better usability.
- Encrypt messages for security.

Enjoy chatting! 🚀
