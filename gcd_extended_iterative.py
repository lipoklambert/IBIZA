def gcd_extended_iterative(a, b):
    # (a,b) = ax + by
    # x0,x1,y0,y1 are the Bezout coefficients
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    # n is used to keep track of the sign of the coefficients
    n = 1
    while( b != 0 ):
        r = a % b  # r is remainder
        q = a // b  # q is the quotient
        a = b  # the divider becomes the dividend in the next while cycle run
        b = r  # the remainder becomes the divider in the next while cycle run
        x = x1
        y = y1
        x1 = q * x1 + x0  # updating x
        y1 = q * y1 + y0  # updating y
        x0 = x  # the current x (x1) becomes the previous x (x0) in the next cycle run
        y0 = y  # the current y (y1) becomes the previous y (y0) in the next cycle run
        n = -n  # changing sign of n
    # if the number of cycle runs is even then n is positive, if it is odd then n is negative
    x = n * x0
    y = -n * y0
    return (a, x, y)