import random


def generate_prime_number():
    while True:
        prime = random.randint(int(900), int(1000))
        if (prime_checker(prime) != -1):
            return prime


def prime_checker(p):
    # Checks If the number entered is a Prime Number or not
    if p <= 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, int(p**0.5)+1):
            if p % i == 0:
                return -1
        return 1


def primitive_check(g, p, L):
    # Checks If The Entered Number Is A Primitive Root Or Not
    for i in range(1, p):
        L.append(pow(g, i) % p)
       # print(f"i: {i}, g: {g}, p: {p}, L: {L}\n")
    for i in range(0, p):
        if L.count(i) > 1:
            L.clear()
            return -1
    return 1


def calculate_public_key(prime, generator, private_key):
    return (generator ** private_key) % prime


def calculate_shared_secret(prime, public_key, private_key):
    return (public_key ** private_key) % prime


def manual_dh():
    P, G, x1 = 0, 0, 0
    while 1:
        P = input("-> Enter P : ")
        if not P.isdigit():
            print("-> Invalid input, try again")
            continue
        P = int(P)
        if prime_checker(P) == -1:
            print("-> Number is not prime, try again")
            continue
        break

    while 1:
        G = input(f"-> Enter the primitive root of {P} : ")
        l=[]
        if not G.isdigit():
            print("-> Invalid input, try again")
            continue
        G = int(G)
        if primitive_check(G, P, l) == -1:
            print(f"-> Number is not a primitive root of {P}, try again")
            continue
        break

    while 1:
        x1 = input("-> Enter private key: ")
        if not x1.isdigit():
            print("-> Invalid input, try again")
            continue
        x1 = int(x1)
        if x1 >= P:
            print(f"-> Private key should be less than {P}")
            continue
        break

    return P, G, x1