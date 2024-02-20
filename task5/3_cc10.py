def f(n):
    a1, a2, a3 = map(int, str(n))
    s = [a1 * 10 + a2, a1 * 10 + a3,
         a2 * 10 + a1, a2 * 10 + a3,
         a3 * 10 + a1, a3 * 10 + a2]
    b = [x for x in s if x >= 10]
    return max(b) - min(b)


for i in range(100, 1000):
    if f(i) == 80:
        print(i)