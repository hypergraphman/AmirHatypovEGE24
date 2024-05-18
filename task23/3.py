def f(s, e):
    if s < e or s == 5 or s == 15:
        return 0
    if s == e:
        return 1
    m = [f(s - 1, e),
         f(s - 4, e),
         f(s // 2, e)]
    return sum(m)


print(f(19, 2))