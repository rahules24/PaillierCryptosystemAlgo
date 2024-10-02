# client.py

import socket
from Paillier import Paillier
import pickle

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the local machine name
    host = 'localhost'
    port = 12345
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send a message to the server
    hello_message = "Hello, Server!"
    client_socket.send(hello_message.encode('utf-8'))
    
    # Receive greeting from the server
    response = client_socket.recv(1024).decode('utf-8')
    print("Received from server:", response)
    
    # run KeyGeneration 
    paillier_object = Paillier()
    public_key, private_key = paillier_object.key_generation(64)
    print("private key generated is : ", public_key)
    print("public key generated is : ", private_key)

    # send the public key to server
    client_socket.send(pickle.dumps(public_key))
    print("sent public key to server:", public_key)

    # encrypt the first message
    m1 = 1000
    c1 = paillier_object.encrypt(public_key, m1)
    print("the first message :", m1)

    # send the encrypted message to server
    client_socket.send(pickle.dumps(c1))
    print("sent first encrypted message to server:", c1)

    # encrypt the second message
    m2 = 2000
    c2 = paillier_object.encrypt(public_key, m2)
    print("the second message :", m2)

    # send the encrypted message to server
    client_socket.send(pickle.dumps(c2))
    print("sent second encrypted message to server:", c2)

    # Receive second encrypted message from the client as int
    result_cipher = client_socket.recv(4096)
    result_cipher = pickle.loads(result_cipher)  # Deserialize the response
    print("Received the result from server", result_cipher)

    # decrypt the result
    result_plain = paillier_object.decrypt(public_key, private_key, result_cipher)
    print("the result message :", result_plain)

    # Close the connection
    client_socket.close()
    print("connection closed.")
    
if __name__ == '__main__':
    start_client()