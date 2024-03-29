from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    alp = digits + ascii_uppercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r


t = n_to_p(8 ** 5 + 4 ** 5 - 16, 2)
print(t.count('1'))
