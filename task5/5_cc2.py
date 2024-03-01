def f(n):
    s1 = bin(n)[2:]
    s2 = s1[1:]
    return int(s2, 2)


r = set()
for i in range(131, 3132):
    r.add(f(i) - i)
print(len(r))
