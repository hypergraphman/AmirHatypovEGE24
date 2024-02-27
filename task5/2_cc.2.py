def f (n):
    s1 = bin(n)[2:]
    s2 = s1 + s1[-1]
    s3 = s2 + str(s2.count('1') % 2)
    return int(s3, 2)


a = []
for i in range(1, 1000):
    if f(i) > 167:
        a.append(f(i))
print(min(a))
