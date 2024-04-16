def f(n):
    if n < 10:
        return n
    if n >= 10:
        return f(n // 10) + n % 10


x = f(131)
for n in range(100, 1000):
    if f(n) < x:
        print(n)