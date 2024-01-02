# InfoSec---Implementing-Cryptosystems
The "Implementing Cryptosystems" project provides a holistic approach to cryptographic solutions, catering to both private and public-key requirements. It seamlessly blends historical methods like the Caesar and Substituting Ciphers with contemporary techniques such as the Vigenère Cipher for enhanced private communication security. Furthermore, it incorporates advanced encryption standards like AES for robust data protection. For secure key establishment and communication, the project employs the Diffie-Hellman Key Exchange and RSA Encryption. With a user-friendly 
interface and built using trusted languages like Python and Java, it guarantees both reliability and ease of use. 


•	server.py and client.py: 
The server code (Client 1) can run remotely on another device and still allow the client to connect to it. It maintains significant control over the entire communication process. Multiple checks are implemented at each step to verify the client's authenticity, with a specialized function, 'authenticate_client,' defined for this purpose.

The code structure permits users on both ends to terminate the connection as needed, and this action is reflected at the top of the terminals for each user.

The server listens on the machine's IP address on a randomly assigned port (12345) and awaits incoming connections. Upon receiving a connection, it prompts the client for a username and password, initiating the authentication process. If the client is validated, the server then prompts the user to select which cryptosystem they wish to proceed with. However, if the client fails authentication, the server informs the client of the invalid credentials. Subsequently, a message is displayed on the terminal, and both the server and client are deliberately shut down.

All subsequent functionalities are integrated with individual Python files for each cryptosystem, which is why you'll find import statements at the top of each file.
Regarding the Client (Client 2), its primary role thus far has been to respond to server messages. However, it doesn't exert significant control over the communication establishment process.


• aes.py and dh.py:
The functionality is segmented into two files: 'aes.py' and 'dh.py'. Each file is responsible for its designated role. The AES feature serves as an enhancement, building upon the existing Diffie-Hellman Key Exchange code.
Users have two methods for generating the shared secret key: automatic and manual, which function exactly as their names suggest. Once the key is successfully generated, the server offers two choices: either continue communication using the key or solely display the key value on the terminal, meant purely for demonstration purposes, before discontinuing further interactions.


•	rsa.py: 
Similar to the previously mentioned Diffie-Hellman cryptosystem, this encryption feature offers users both manual and automatic options to streamline the encryption process.
Once the public key is generated, it is transmitted to the client. Subsequently, the client is prompted to provide a message for encryption, intended for transmission to the server.
Upon receiving the encrypted message, the server decrypts it using its private key and then displays the deciphered message on the terminal.


•	caesar.py:
Historically, this cipher holds significant importance, yet it's relatively vulnerable to simple brute-force techniques, making it obsolete in today's digital era.
In this cipher, the user provides a shift value that dictates the encryption method for the entire message. The server terminal prompts the user for the message, which is then encrypted using the specified shift value. After encrypting the message, along with the shift value, the server transmits it to the client. The client subsequently decrypts the message and showcases it on its terminal.


•	substitution.py: 
Much like the Caesar cipher, this cipher holds historical significance but is susceptible to brute-force attacks if not complemented by modern encryption standards.
For this cipher, the user provides a 26-alphabet key, with customized exception handling implemented to manage improper inputs. The fundamental principle involves correlating each position of the standard alphabet with the provided key for encryption. Conversely, decryption follows the inverse process.


•	vigenère.py:
Continuing with our exploration, the Vigenère cipher stands out as another significant cipher, closely resembling the substitution cipher but distinguished by a pivotal difference.
For the Vigenère cipher, a 26-alphabet key is provided as input. This key determines the relative spacing from 'A', serving as the shift value for encoding the user's message by adding its value to the numeric value of the respective alphabets. Both the encoded message and the 26-alphabet key are then transmitted to the client for decryption.
As reiterated previously, while these ciphers hold historical importance, they are susceptible to decryption and should be used cautiously to maintain data security.


•	test.py: 
This file served as the testing platform for small code snippets. These snippets couldn't be executed in the original files due to complexities and potential clashes with other parts of the code. Commenting them out would disrupt the predetermined flow of control.


•	gui.py: 
A sample GUI interface is included in the GitHub repository. This serves as an example GUI that could be implemented to enhance user experience, streamline the process, and prove to be an invaluable asset.
