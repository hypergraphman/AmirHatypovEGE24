from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * f(n - 1) + g(n - 1) - n

@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return 3 * f(n - 1) - 2 * g(n - 1) + n


for n in range(1, 10000):
    g(n)

print(sum(map(int, str(g(33))[1:])))