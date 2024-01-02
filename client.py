import socket
import random
import dh
import aes
import caesar
import substitution
import vigenère

# Driver code
def run_client():
    global y1, P, G

    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("\nPress 'Ctrl + C' to abort")
    server_ip = input("Enter server IP address: ")  # Server's IP address
    server_port = 12345  # Server's port number
    
    try:
        # Establish connection with server
        client.connect((server_ip, server_port))
        print("Connection to server successful")

        username = input("\nEnter username: ")
        password = input("Enter password: ")

        client.send(f"{username}".encode("utf-8")[:1024]) # 1st send
        client.send(f"{password}".encode("utf-8")[:1024]) # 2nd send

        response = client.recv(1024).decode("utf-8") # 1st receive
        if response == "0":
            print("\nClient authentication rejected")
            return
        else:
            print("\nClient authentication complete\n")
 
        while True:
            # Receive chosen option response from the server
            response = client.recv(1024).decode("utf-8") # 2nd receive (ans)

            if response == "1":
                x2 = 0
                type = client.recv(1024).decode("utf-8") # 3rd receive (ans)

                # Receive public key of server, the decided prime and primitive modulo of the prime
                data = client.recv(1024).decode("utf-8") # 4th receive
                y1 = int(data.split(',')[0])   # Public key of server
                P = int(data.split(',')[1])    # Prime number
                G = int(data.split(',')[2])    # Primitive modulo of the prime number

                # Manual
                if type == "m":
                    while 1:
                        x2 = int(input("\n1) Enter private key: "))
                        if x2 >= P:
                            print(f"-> Private key should be less than {P}")
                            continue
                        break

                # Automatic
                else:
                    x2 = random.randint(1, P - 1)
                    print("\n1) Private key generated")

                y2 = dh.calculate_public_key(P, G, x2)

                # Send public key of client to server
                client.send(f"{y2}".encode("utf-8")[:1024]) # 3rd send (y2)

                # Calculate the shared secret key
                print("-> Calculating shared secret key")
                k = dh.calculate_shared_secret(P, y1, x2)
                print("-> Shared secret key calculated")
                
                # Receive option to continue with RSA
                opt = client.recv(1024).decode("utf-8") # 5th receive

                if (opt.lower() == 'n'):

                    # Print the shared secret key
                    print(f"\n  [Shared secret key: {k}]\n")

                else:

                    # Receive encrypted message from other client
                    encr = client.recv(1024).decode("utf-8") # 6th receive
                    print("-> Received encrypted client message")

                    # Decrypt the encrypted message
                    print("-> Decrypting client message")
                    decr = aes.decrypt(k, encr)

                    print(f"\n  [Decrypted message: {decr}]\n")

            elif response == "2":

                # Receive public key of server, the decided prime and primitive modulo of the prime
                data = client.recv(1024).decode("utf-8") # 3rd receive
                e = int(data.split(',')[0])    # receive e
                n = int(data.split(',')[1])    # receive n

                print("\n2) Public key received")

                while 1: 
                    s = input("-> Enter message to encrypt: ")

                    if not s:
                        print("-> Empty string evaluated, try again")
                    else:
                        break

                # Send length of string to other client
                client.send(str(len(s)).encode("utf-8")[:1024]) # 3rd send (len)

                # Encrypt the unpadded string
                encr = ""
                for i in range(len(s)):
                    encr += f"{(ord(s[i])**e) % n},"
                
                # Send the encrypted string to other client
                client.send(encr.encode("utf-8")[:1024]) # 4th send (encr)
                print("-> Encrypted message sent to other client")
                    
            elif response == "3":

                # Receive the shift value from the other client
                n = client.recv(1024).decode("utf-8") # 3rd receive (n)

                # Receive the encrypted message from the other client
                s = client.recv(1024).decode("utf-8") # 4th receive (ans)
                print(f"\n3) Received shift value and encrypted message from other client")

                # Decrypt the encrypted message
                print("-> Decrypting client message")
                decr = caesar.decrypt(s, n)
                
                print(f"\n  [Decrypted message: {decr}]\n")

            elif response == "4":

                # Receive the key from the other client
                key = client.recv(1024).decode("utf-8") # 3rd receive (key)

                # Receive the translated message from the other client
                translated = client.recv(1024).decode("utf-8") # 4th receive (translated)
                print(f"\n4) Received key and encrypted message from other client")

                # Decrypt the encrypted message
                print("-> Decrypting client message")
                decr = substitution.translateMessage(translated, key, "d")

                print(f"\n  [Decrypted message: {decr}]\n")

            elif response == "5":

                # Receive the key from the other client
                key = client.recv(1024).decode("utf-8") # 3rd receive (key)

                # Receive the translated message from the other client
                translated = client.recv(1024).decode("utf-8") # 4th receive (translated)
                print(f"\n5) Received key and encrypted message from other client")

                # Decrypt the encrypted message
                print("-> Decrypting client message")
                decr = vigenère.vigenere_cipher_decrypt(translated, key)

                print(f"\n  [Decrypted message: {decr}]\n")

    except Exception as e:
        print(f"\nError: {e}")

    finally:
        # Close client socket (connection to the server)
        print("Connection to server closed\n")
        client.close()
             
run_client()