from random import randrange
from modpow import modpow


def MillerRabinTest2(n, m):
    a = randrange(2, n-2)  #randrange function is used to generate a random integer between 2 and n-2
    x = modpow(a, m, n)
    if x == 1 or x == n-1:
        return True
    while m != n-1:
        x = x**2 % n
        m = m*2
        if x == 1:
            return False
        if x == n-1:
            return True
    return False


def isPrime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    m = n-1
    while(m % 2 == 0):
        m = m // 2
    for i in range(k):
        if not MillerRabinTest2(n, m):
            return False
    return True