import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


BLOCK_SIZE = AES.block_size


def generate_key(key):

    # Brief: Hashing the given key, gives the same output everytime for the same key
    """ Hashes the key using the SHA-256 algorithm and 
        returns the hashed byte sequence, which acts as 
        the AES encryption key """
    return hashlib.sha256(str(key).encode()).digest() 


def pad(plain_text):
    number_of_bytes_to_pad = BLOCK_SIZE - len(plain_text) % BLOCK_SIZE
    ascii_string = chr(number_of_bytes_to_pad)

    # Since each ASCII character is 1 byte long
    padding_str = number_of_bytes_to_pad * ascii_string 
    return plain_text + padding_str


def unpad(plain_text):
    last_character = plain_text[len(plain_text) - 1:]

    # Brief: Slicing uses negative indices to count from the end of the string
    """ Means that you're slicing up to (but not including) 
    the position that corresponds to the Unicode code point
    value of last_character from the end of the string """
    return plain_text[:-ord(last_character)] 


# (add padding) -> (encode(to bytes) -> encrypt) -> (add IV -> encode(base64)) 
# .decode() is for printing in a human-readable format and has no other active contribution
def encrypt(key, plain_text):
    key = generate_key(key)
    plain_text = pad(plain_text)

    """ Inititalization Vector: Ensures that each 
    encrypted message produces a unique ciphertext, 
    even if the same plaintext is encrypted multiple times """
    iv = Random.new().read(BLOCK_SIZE)

    # Create a cipher using the hashed key and the IV to encrypt data
    # -Will give the same cipher everytime for the same hashed key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # .encode() converts a Unicode string into a sequence of bytes; Default UTF-8
    encrypted_text = cipher.encrypt(plain_text.encode())

    # The IV along with the encrypted text is encoded using base64 and returned as a string
    # -As a string for the client to read
    return b64encode(iv + encrypted_text).decode("utf-8")


# decode(base64) -> extract IV -> decrypt -> decode(to string) -> remove padding
def decrypt(key, encrypted_text):
    key = generate_key(key)
    encrypted_text = b64decode(encrypted_text)

    # Not including 'BLOCK_SIZE' since Python uses 0-based indexing
    iv = encrypted_text[:BLOCK_SIZE]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = cipher.decrypt(encrypted_text[BLOCK_SIZE:]).decode("utf-8")
    return unpad(plain_text)