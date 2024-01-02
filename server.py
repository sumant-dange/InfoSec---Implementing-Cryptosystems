import socket
import random
import dh
import aes
import rsa
import caesar
import substitution
import vigenère


USER_DATABASE = {
    'user1': 'password1',
    'user2': 'password2'
}


def authenticate_client():
    """Authenticate the client based on username and password."""
    username = client_socket.recv(1024).decode("utf-8")
    password = client_socket.recv(1024).decode("utf-8")

    if username in USER_DATABASE and USER_DATABASE[username] == password:
        client_socket.send("1".encode("utf-8"))
        return True
    else:
        client_socket.send("0".encode("utf-8"))
        return False


# Driver code
def run_server():
    server_ip = str(socket.gethostbyname(socket.gethostname()))  # Server hostname or IP address
    port = 12345  # Server port number

    # Create a socket object
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the host and port
        server.bind((server_ip, port))

        # Listen for incoming connections
        server.listen()
        print("\nServer initialized")
        print(f"Listening on {server_ip}:{port}")
        print("Waiting for incoming connections")

        # Accept incoming connections
        global client_socket
        client_socket, client_address = server.accept()
        print(f"\nIncoming connection from {client_address[0]}:{client_address[1]}")

        # Authenticate the client
        print("Authenticating client")
        authenticated = authenticate_client()
        if not authenticated:
            print("Client authentication failed, invalid credentials")
            client_socket.close()
            return
        
        print("Client authentication validated")
        print("Logging in")
        print("\nPress 'Ctrl + C' or type 'close' when prompted to abort\n")
        
        while 1:
            print("\n1. AES-encrypted Diffie-Hellman Key Exchange")
            print("2. RSA Encryption")
            print("3. Caesar Cipher")
            print("4. Substitution Cipher")
            print("5. Vigenère Cipher")
            ans = input("Enter the associated number for the process you wish to proceed with or type 'close' to abort: ")

            if ans.lower() == "close":
                return
            
            if not ans.isdigit():
                print("Invalid input, try again\n")
                continue

            ans = int(ans)

            if ans == 1:

                k = 0
                client_socket.send("1".encode("utf-8")) # 1st send (response)

                while 1: 
                    P, G, x1 = 0, 0, 0
                    ans = input("\n1) Do you want to automate the process? Type y/n: ")
                    if (ans.lower() == "n"):

                        # Tell the client that we'll be working through this manually
                        client_socket.send("m".encode("utf-8")) # 2nd send (type)

                        # Decide on P, G and private key of server
                        P, G, x1 = dh.manual_dh()

                    elif ans.lower() == "y":

                        # Tell the client that the process is automated
                        client_socket.send("a".encode("utf-8")) # 2nd send (type)

                        P = dh.generate_prime_number()
                        l=[]
                        while 1:
                            G = random.randint(2, P - 1)
                            if(dh.primitive_check(G,P,l) == 1):
                                break

                        x1 = random.randint(1, P - 1)

                    else:
                        print("-> Invalid input, try again")
                        continue

                    # Calculate public key of server
                    y1 = dh.calculate_public_key(P, G, x1)

                    # Send public key of server, prime and the primitive modulo to client
                    client_socket.send(f"{y1},{P},{G}".encode("utf-8")) # 3rd send

                    print("-> Standby for public key of other client")
                    
                    # Receive public key of the client
                    y2 = int(client_socket.recv(1024).decode("utf-8")) # 1st receive (y2)
                    print("-> Public key of other client received")

                    # Calculate the shared secret key
                    print("-> Calculating shared secret key")
                    k = dh.calculate_shared_secret(P, y2, x1)
                    print("-> Shared secret key calculated")
                    break

                while 1:
                    ans = input("\nDo you want to communicate (AES-encrypted) with the other client using the shared key? Type y/n: ")
                    if (ans.lower() == "n"):

                        client_socket.send("n".encode("utf-8")) # 4th send (opt)

                        # Print the shared secret key
                        print(f"\n  [Shared secret key: {k}]\n")

                    elif (ans.lower() == "y"):

                        client_socket.send("y".encode("utf-8")) # 4th send (opt)

                        message = input("-> Enter message to encrypt: ")
                        encrypted = aes.encrypt(k, message)
                        
                        # Send encrypted message to other client
                        client_socket.send(f"{encrypted}".encode("utf-8")) # 5th send (encr)
                        print("-> Encrypted message sent to other client\n")

                    else:
                        print("-> Invalid input, try again")
                        continue
                    break

            elif ans == 2:

                client_socket.send("2".encode("utf-8")) # 1st send (response)
                
                e, d, n = 0, 0, 0

                while 1: 
                    ans = input("\n2) Do you want to automate the process? Type y/n: ")
                    if ans.lower() == "n":

                        # Decide on 'p', 'q', 'e' and get 'e', 'd' and 'n' in return
                        e, d, n = rsa.manual_rsa()

                    elif ans.lower() == "y":
                        print("-> Computation might take at most 1 minute, please wait")

                        # Decide on 'p', 'q', 'e' and get 'e', 'd' and 'n' in return
                        e, d, n = rsa.automate_rsa()

                    else:
                        print("-> Invalid input, try again")
                        continue

                    # Send 'e' and 'n' to client
                    print("-> Public-private key pair generated")
                    client_socket.send(f"{e},{n}".encode("utf-8")) # 2nd send 
                    break

                print("-> Standby for client input")

                # Receive length of the encrypted string
                len = int(client_socket.recv(1024).decode("utf-8")) # 1st receive (len(s))

                # Receive the encrypted string
                encr = client_socket.recv(1024).decode("utf-8") # 2nd receive (encr)
                print("-> Client message received")

                # Decrypt the encrypted string
                print("-> Decrypting client message")
                decr = ""
                
                for i in range(len):
                    x = int(encr.split(',')[i])
                    decr += chr((x ** d) % n)
                
                print(f"\n  [Decrypted message: {decr}]\n")

            elif ans == 3:

                client_socket.send("3".encode("utf-8")) # 1st send (response)

                # Get shift and encrypted message from user
                n, ans = caesar.run_caesar()

                # Send shift value to the other client
                client_socket.send(str(n).encode("utf-8")) # 2nd send (n)       
                
                # Send encrypted string to the other client
                client_socket.send(ans.encode("utf-8")) # 3rd send (s)

                print("-> Shift and encrypted message sent to other client\n")

            elif ans == 4:

                client_socket.send("4".encode("utf-8")) # 1st send (response)

                # Get key and translated message from user
                key, translated = substitution.run_substitution()

                # Send key to the other client
                client_socket.send(key.encode("utf-8")) # 2nd send (key)

                # Send translated message to the other client
                client_socket.send(translated.encode("utf-8")) # 3rd send (response)

                print("-> Key and translated message sent to other client\n")
                
            elif ans == 5:

                client_socket.send("5".encode("utf-8")) # 1st send (response) 

                # Get key and translated message from user
                key, translated = vigenère.run_vigenère()

                # Send key to the other client
                client_socket.send(key.encode("utf-8")) # 2nd send (key)

                # Send translated message to the other client
                client_socket.send(translated.encode("utf-8")) # 3rd send (response)

                print("-> Key and translated message sent to other client\n")
             
        # Close connection socket with client
        client_socket.close()
        print("Connection to client closed")

    except Exception as e:
        print(f"\nError: {e}")

    finally:
        # Close server
        print(f"Shutting down\n")
        server.close()

run_server()

