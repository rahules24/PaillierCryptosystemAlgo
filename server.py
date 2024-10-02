# server.py

import socket
from Paillier import Paillier
import pickle
def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the local machine name
    host = 'localhost'
    port = 12345
    
    # Bind the socket to the port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    print("Server is listening on port", port)
    
    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print("Got a connection from", addr)
        
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        print("Received message:", data)
        
        # Send a response back to the client
        client_socket.send("Thank you for connecting".encode('utf-8'))
        
        # Receive public key from the client
        public_key = client_socket.recv(4096)
        public_key = pickle.loads(public_key)  # Deserialize the response
        print("Received public key:", public_key)

        n = public_key[0]

        # Receive encrypted message from the client as int
        c1 = client_socket.recv(4096)
        c1 = pickle.loads(c1)  # Deserialize the response
        print("Received the first encrypted message from client", c1)

        # Receive second encrypted message from the client as int
        c2 = client_socket.recv(4096)
        c2 = pickle.loads(c2)  # Deserialize the response
        print("Received the second encrypted message from client", c2)

        # decrypt the result message
        result =  (c1 * c2) % (n*n)
        # send the encrypted message to server
        client_socket.send(pickle.dumps(result))
        print("sent the result message to client:", result)

        # Close the connection
        client_socket.close()

if __name__ == '__main__':
    start_server()