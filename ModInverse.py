def ModInverse(a,m):
    m0 = m
    x = 1
    y = 0
    # If the modulus m is 1, the function returns 0 because there is no inverse of a modulo 1
    if m == 1:
        return 0
    while(a > 1):
        q = a // m  # q is quotient 
        b = m  # to swap a and m
        m = a % m  # m is remainder
        a = b  # a becomes what was m (before the % operation)
        b = y  # store the value of y in a temporary variable b
        y = x - q * y  # update y to x - q * y
        x = b  # update x to b
    # after the loop has finished, the function checks whether x is negative, and if it is, adds m0 to x. 
    # This ensures that the result returned by the function is a non-negative integer
    if x < 0:
        x += m0
    # the function returns the value of x, which is the modular multiplicative inverse of a modulo m.
    return x