def f(n):
    # a = list(map(lambda x: int(x[0] + x[1]), zip(str(n), str(n)[1:])))
    a = []
    s = str(n)
    for i in range(len(s) - 1):
        a.append(int(s[i] + s[i + 1]))
    return max(a) + min(a)


for i in range(10, 10000):
    if f(i) == 131:
        print(i)
        break
