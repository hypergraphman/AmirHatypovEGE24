from string import digits, ascii_uppercase

def n_to_p(n, p):
    r = ('')
    alp = digits + ascii_uppercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r

t = n_to_p(2 ** 2025 + 4 ** 2024 - 2 ** 2023, 2)
print(t.count('0'))