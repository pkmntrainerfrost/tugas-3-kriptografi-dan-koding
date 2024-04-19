import math
import sympy
import random

# Pembangkit kunci - mengembalikan pasangan kunci publik dan kunci privat
def rsaGenerateKeyPair(p : int = 0, q : int = 0, e : int = 0):
    
    # Cek prima bila dimasukkan secara manual
    if (p != 0 and not (sympy.isprime(p))) or (q != 0 and not (sympy.isprime(q))):
        raise ValueError("P dan Q harus berupa bilangan prima!")
    
    # Cek ketidaksamaan P dan Q bila dimasukkan secara manual
    if p == q and p != 0:
        raise ValueError("P dan Q harus berbeda!")
    
    # Pembangkitan P dan Q secara acak
    while p == 0 or p == q:
        p = sympy.randprime(1,1000)
    while q == 0 or p == q:
        q = sympy.randprime(1,1000)
    
    # Hitung N dan Totient
    n = p * q
    t = (p - 1) * (q - 1)

    # Cek koprima
    if e != 0 and math.gcd(e,t) != 1:
        raise ValueError("Nilai E yang dimasukkan tidak koprima dengan totient!")

    # Pembangkitan E secara acak
    while e == 0 or math.gcd(e,t) != 1:
        e = random.randrange(2,t)

    # Pembangkitan D
    d = pow(e,-1,t)

    return {"public" : {"e" : e,"n" : n}, "private" : {"d" : d,"n": n}}

# Enkripsi
def rsaEncrypt(m : int, public_key : dict):

    if (m < 0):
        raise ValueError("M tidak boleh negatif!")
    if (m >= public_key["n"] - 1):
        raise ValueError("M tidak boleh lebih dari atau sama dengan N + 1!")
    
    return (pow(m,public_key["e"]) % public_key["n"])

# Dekripsi
def rsaDecrypt(c : int, private_key : dict):

    if (c < 0):
        raise ValueError("C tidak boleh negatif!")
    if (c >= private_key["n"] - 1):
        raise ValueError("C tidak boleh lebih dari atau sama dengan N + 1!")
    
    return (pow(c,private_key["d"]) % private_key["n"])

# Driver
if __name__ == "__main__":

    keys = rsaGenerateKeyPair()

    print(keys)

    x = rsaEncrypt(69,keys["public"])

    print(x)
    print(rsaDecrypt(x,keys["private"]))