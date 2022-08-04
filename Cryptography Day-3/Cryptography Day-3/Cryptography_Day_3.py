from asyncio.windows_events import NULL
import random
import re
def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True
        for num in range(2, n):
            if n % num == 0:
                isPrime = False
        if isPrime:
            prime_list.append(n) 
    return prime_list
p = 0 
q = 0
n = 0
e = 0
d = 0
decryptiondone = False
decrypted = ""
encrypted = ""
primeselect = 0
primelist = []
mode = ""
while True:
    print("Hello, Would you like to (E)ncrypt, (D)ecrypt or (Q)uit?")
    mode = input()
    if mode == "E" or mode == "e":
        print("Level of encryption? \n(L)ow, (M)edium, (H)igh")
        enlvl = input()
        if enlvl == "L" or mode == "l":
            primelist = primesInRange(2, 250)
            primeselect = random.randrange(1,50)
            p = primelist[primeselect]
            primeselect = random.randrange(1,50)
        if enlvl == "M" or mode == "m":
            primelist = primesInRange(2, 500)
            primeselect = random.randrange(1,93)
            p = primelist[primeselect]
            primeselect = random.randrange(1,93)
        if enlvl == "H" or mode == "h":
            primelist = primesInRange(2, 1000)
            primeselect = random.randrange(1,165)
            p = primelist[primeselect]
            primeselect = random.randrange(1,165)
        q = primelist[primeselect]
        n = p * q
        e = ((p - 1) * (q - 1)) - 1
        print("Text to be encrypted?")
        decrypted = input()
        for i in decrypted:
            encrypted += chr(((ord(i) ^ e) % n))
        decrypted = ""
        print("Private Key: " + str(d) + ", " + str(n))
        print("Encrypted message: "+ encrypted + "\n")
    if mode == "D" or mode == "d":
        print("Encrypted message?")
        encrypted = input()
        print("Private Key?\nFormat as: 'x, y'")
        keys = input()
        keys = keys.split(', ')
        d = int(keys[0])
        n = int(keys[1])
        print(keys[0])
        print(keys[1])
        while decryptiondone == False:
            if ((e * d) % (e + 1)) == 1:
                for i in encrypted:
                    decrypted += chr(((ord(i) ^ d) % n))
                decryptiondone = True
            else:
                d = d + 1
        print(decrypted + "\n")
    if mode == "Q" or mode == "q":
        quit()