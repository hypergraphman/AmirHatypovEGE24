from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    alp = digits + ascii_uppercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n, 3)
    s2 = s1 + str(n % 3)
    s3 = s2 + str(n % 3)
    s4 = s3 + str(n % 3)
    return int(s4, 3)


print(f(131))
a = []
for i in range(1, 131):
    if f(i) > 999:
        a.append(f(i))
print(min(a))