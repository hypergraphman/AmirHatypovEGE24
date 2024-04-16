def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 5 == 0:
        return f(n / 5) + 5
    if n >= 2 and n % 5 != 0:
        return f(n - 3) + 5

for n in range(1, 1000):
    if f(n) < 10 ** 5:
