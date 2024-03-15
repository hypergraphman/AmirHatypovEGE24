from string import  digits, ascii_uppercase
def n_to_p(n, p):
    r = ''
    alp = digits + ascii_uppercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r

def f(n):
    s1 = n_to_p(n, 3)
    if n % 3 == 0:
        s2 = '1' + s1 + '02'
    elif n % 3 != 0:
        s0 = n % 3 * 4
        s2 = s1 + n_to_p(s0, 3)
    return int(s2, 3)


a = []
for i in range(1, 1000):
    if f(i) < 1199:
        a.append(i)
print(max(a))