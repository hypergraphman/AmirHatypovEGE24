def f(n):
    # a1, a2, a3 = n // 100, n // 10 % 10, n % 10
    a1, a2, a3 = map(int, str(n))
    s1 = a1 + a2
    s2 = a2 + a3
    if s1 > s2:
        return str(s1) + str(s2)
    else:
        return str(s2) + str(s1)


for i in range(100, 1000):
    if f(i) == '145':
        print(i)
        break