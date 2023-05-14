from Miller_Rabin import isPrime
import random
from gcd_extended_iterative import gcd_extended_iterative
from modpow import modpow
from ModInverse import ModInverse

def get_rand_primes(bits=512):
    """
    This function generates two random prime numbers, p and q, with 'bits' number of bits.
      It does this by repeatedly generating random numbers until it finds two prime numbers.
        The isPrime function is called to check whether a number is prime.
    """
    p = random.getrandbits(bits)
    q = random.getrandbits(bits)
    while not isPrime(p, 1):
        p = random.getrandbits(bits)
    while not isPrime(q, 1):
        q = random.getrandbits(bits)
    return(p, q)


def init():
    """
    This function initializes the RSA encryption scheme. 
    It generates p and q using the get_rand_primes() function, calculates the modulus n and the totient phi,
    and then selects a public exponent e that is relatively prime to phi. 
    The gcd_extended_iterative function is used to compute the greatest common divisor of e and phi and the modular inverse of e modulo phi,
    which is the private exponent d.
    """
    p, q= get_rand_primes()
    n = p * q
    phi = (p-1) * (q-1)
    e = random.getrandbits(512)
    while gcd_extended_iterative(phi, e)[0] != 1 or e > phi:
        e = random.getrandbits(512)
    d = ModInverse(e, phi)
    return n, e, d


def encrypt(msg, e, n):
    """
    This function takes a message msg and encrypts it using the public exponent e and modulus n.
    The function returns the ciphertext.
    """
    return modpow(msg, e, n)


def decrypt(cipher, d, n):
    """
    This function takes a ciphertext cipher and decrypts it using the private exponent d and modulus n.
    The function returns the decrypted message.
    """
    return modpow(cipher, d, n)


n, e, d = init()

ciphertest = encrypt(8,e,n)
print(ciphertest)
print(decrypt(ciphertest, d, n))
