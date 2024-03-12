from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    alp = digits + ascii_uppercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r

def f(n):
    s1 = n_to_p(n, 4)
    if n % 2 != 0:
        s2 = '2' + s1 + '11'
    else:
        s2 = '13' + s1 + '02'
    return int(s2, 4)


print(f(45))

a = []
for i in range(1, 2773):
    if f(i) > 1000:
        a.append(f(i))
print(min(a))

