def encrypt(s, n):
    result = ""
 
    # traverse text
    for i in range(len(s)):
        char = s[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 + n) % 26 + 65)
 
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 + n) % 26 + 97)

        else:
            result += char
 
    return result


def decrypt(s, n):
    result = ""
    n = int(n)

    # traverse text
    for i in range(len(s)):
        char = s[i]
        
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 - n) % 26 + 65)
 
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 - n) % 26 + 97)

        else:
            result += char
 
    return result


# Driver code
def run_caesar():
    n = 0
    while 1: 
        s = input("\n3) Enter message to encrypt: ")

        if not s:
            print("-> Empty string evaluated, try again")
        else:
            break

    while 1:
        n = input("-> Enter the right shift: ")
        if not n.isdigit():
            print("-> Invalid input, try again")
        else:
            n = int(n)
            break
        
    ans = encrypt(s, n)

    print(f"-> Message encrypted")

    return n, ans