def f(q, p):
    if p == 0:
        return q
    if p > 0:
        return f(p, (q % p))


k = 0
for q in range(50, 251):
    for p in range(50, 251):
        if f(q, p) == 25:
            k += 1
            break

print(k)
