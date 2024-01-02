import random
import dh


def lcm(num1, num2):
    lcm=0
    for i in range(max(num1, num2), 1 + (num1 * num2)):
        if i % num1 == i % num2 == 0:
            lcm = i
            break
    return lcm


def automate_rsa():
    p = dh.generate_prime_number()
    q = dh.generate_prime_number()
    n = p*q
    l = lcm(p-1, q-1)
    while 1:
        e = random.randint(2, int(l**(0.5)))
        if e == 2 or e == int(l**(0.5)):
            continue
        if (e*l)/lcm(e,l) != 1:
            continue
        break

    d=0
    for X in range(1, l):
        if((e%l)*X)%l == 1:
            d=X

    return e, d, n


def manual_rsa():
    
    p, q, e = 0, 0, 0

    # Take the prime numbers from the user
    while 1:
        print("  --------------------------------------------------------------------------------------")
        print("   CAUTION! RSA might break for prime numbers less than 20, continue at your discretion")
        print("  --------------------------------------------------------------------------------------")
        p = input("-> Enter 1st prime number: ")
        if not p.isdigit():
            print("-> Invalid input, try again")
            continue
        p=int(p)
        if dh.prime_checker(p) == -1:
            print("-> Number isn't prime, try again")
            continue
        break

    while 1:
        q = input("-> Enter 2nd prime number: ")
        if not q.isdigit():
            print("-> Invalid input, try again")
            continue
        q=int(q)
        if dh.prime_checker(q) == -1:
            print("-> Number isn't prime, try again")
            continue
        if p == q:
            print("-> Prime numbers can't be same, try again")
            continue
        break

    # Calculate the modulus for encryption
    n = p*q

    # Calculate Carmichael's totient function 
    l = lcm(p-1, q-1)

    # Take e from user
    while 1:
        e = input(f"-> Enter e between 2 and {l}, and coprime with {l}: ")
        if not e.isdigit():
            print("-> Invalid input, try again")
            continue
        e = int(e)
        if e<=2 or e>=l:                                 # Check if 2<e<l
            print(f"-> 'e' should be between 2 and {l}, try again")
            continue
        elif (e*l)/lcm(e,l) != 1:                        # Check if e is coprime with l
            print(f"-> 'e' should be coprime with {l}, try again")
            continue
        break

    # Calculate modular multiplicative inverse 'd'
    d=0
    for X in range(1, l):
        if((e%l)*X)%l == 1:
            d=X

    return e, d, n