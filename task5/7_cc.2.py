def f(n):
    s1 = bin(n)[2:]
    if s1.count('1') > s1.count('0'):
        s2 = s1 + '1'
    else:
        s2 = s1 + '0'
    return int(s2, 2)


a = []
for i in range(1, 1000):
    if f(i) > 100:
        a.append(f(i))
print(min(a))
