def f(n):
    # s1 = sum(map(int, filter(lambda x: x in '02468', str(n))))
    s1 = 0
    for c in str(n):
        if c in '02468':
            s1 += int(c)
    # s2 = sum(map(int, str(n)[1::2]))
    s2 = 0
    for c in str(n)[1::2]:
        s2 += int(c)
    return abs(s1 - s2)


for i in range(1, 10000000):
    if f(i) == 17:
        print(i)
        break
