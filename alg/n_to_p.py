from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    alp = digits + ascii_uppercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r


# print(n_to_p(194, 2), bin(194)[2:])
# print(n_to_p(194, 5), 1234)
# print(n_to_p(255, 16), hex(255)[2:])