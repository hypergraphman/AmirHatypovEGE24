def f(n):
    s1 = bin(n)[2:]
    s2 = s1 + str(s1.count('1') % 2)
    s3 = s2 + str(s2.count('1') % 2)
    return int(s3, 2)


a = []
for i in range(1, 1000):
    if f(i) > 48:
        a.append(f(i))
print(min(a))