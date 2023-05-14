def modpow(a, e, m):
    result = 1
    apow = a
    while(e != 0):
        #This code is checking the least significant bit of the value e by performing
        #  a bitwise AND operation with the hexadecimal value 0x01. The bitwise AND operation compares each bit of e
        #  with the corresponding bit of 0x01, and if both bits are 1, the resulting bit is 1. Otherwise, the resulting bit is 0.
        if e & 0x01 == 0x01:
            result = (result * apow) % m

        #These two lines shift e one bit to the right and square apow modulo m. 
        # This computes the next power of a that we need for the next bit position of e.
        e >>= 1
        apow = (apow * apow) % m

    return result