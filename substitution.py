import random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getRandomKey():
   randomList = list(LETTERS)
   random.shuffle(randomList)
   return ''.join(randomList)


def translateMessage(message, key, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
   
    # If decrypt mode is detected, swap A and B
    if mode == "d":
       charsA, charsB = charsB, charsA

    for symbol in message:

        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())

            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol

    return translated
      

# Store the key into list, sort it, convert back, compare to alphabet
def checkKey(key):
   keyString = ''.join(sorted(list(key)))
   return keyString.upper() == LETTERS


# Driver code
def run_substitution():
    
    while 1: 
        message = input("\n4)  Enter message to encrypt: ")

        if not message:
            print("-> Empty string evaluated, try again")
        else:
            break

    key = ''

    while checkKey(key) is False:
        key = input("-> Enter 26 alphabet key (leave blank for random key): ")

        if key == '':
            key = getRandomKey()
            print(f"-> Using key: {key}")
        if checkKey(key) is False:
            print("-> There is an error in the key or symbol set")

    key = key.upper()

    translated = translateMessage(message, key, "e")
    
    print(f"-> Message encrypted")

    return key, translated