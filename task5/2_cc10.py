def f(n):
    a1,a2,a3,a4,a5 = map(int, str(n))
    s1 = a1 + a3 + a5
    s2 = a2 + a4
    if s1 > s2:
        return str(s2) + str(s1)
    else:
        return str(s1) + str(s2)


for i in range(10000, 100000):
    if f(i) == '321':
        print(i)
        break
