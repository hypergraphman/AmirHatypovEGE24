from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return f(0) + 1
    if n > 2:
        return f(n - 1) + f(n - 2) + f(n - 3)


for n in range(1, 1310):
    f(n)

print(f(1310))