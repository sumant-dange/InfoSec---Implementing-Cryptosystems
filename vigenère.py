import random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getRandomKey():
   randomList = list(LETTERS)
   random.shuffle(randomList)
   return ''.join(randomList)



def checkKey(key):
    for i in range(len(key)):
        char = key[i]
        if not char.isalpha():
            return False
    return True


def vigenere_cipher_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            elif char.islower():
                encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text


def vigenere_cipher_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - key_shift + 26) % 26 + ord('A'))
            elif char.islower():
                decrypted_text += chr((ord(char) - ord('a') - key_shift + 26) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text


# Driver code
def run_vigenère():

    while 1: 
        message = input("\n5)  Enter message to encrypt: ")

        if not message:
            print("-> Empty string evaluated, try again")
        else:
            break

    key = ''

    while 1:
        key = input("-> Enter polyalphabetic key (leave blank for random key): ")

        if key == '':
            key = getRandomKey()
            break
        if len(key) > 26:
            print("-> Key must not exceed 26 letters in length, try again")
        if checkKey(key) is False:
            print("-> Key should exclusively contain characters, try again")
        else:
            break

    print(f"-> Using key: {key}")

    translated = vigenere_cipher_encrypt(message, key)

    print(f"-> Message encrypted")
    
    return key, translated