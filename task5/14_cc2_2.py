def h(s):
    if s.count('1') % 2 == 0:
        r = s[1:].lstrip('0')
        if r == '':
            r = '0'
    else:
        r = s.replace('0', '') + '1'
    return r


def f(n):
    s1 = bin(n)[2:]
    s2 = h(s1)
    s3 = h(s2)
    return int(s3, 2)


# print(f(5))
k = 0
for i in range(1, 1000 + 1):
    if f(i) == 7:
        k += 1
print(k)