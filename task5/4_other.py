from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    alp = digits + ascii_uppercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n, 7)
    s2 = '10' + s1[2:] + n_to_p(sum(map(int, s1)), 7)
    s3 = '100' + s2[3:] + n_to_p(sum(map(int, s2)), 7)
    s4 = '1000' + s3[4:] + n_to_p(sum(map(int, s3)), 7)
    return int(s4, 7)


a = []
for i in range(1,100000):
    if f(i) > 100000:
        a.append(f(i))
print(min(a))
