def f(n):
    s1 = bin(n)[2:]
    s2 = s1[::-1]
    return int(s2, 2)


for i in range(1, 201):
    if f(i) == 21:
        print(i)

