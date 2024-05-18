def f(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    m = [f(s - 1, e)]
    if s % 2 == 0:
        m.append(f(s // 2, e))
    if s % 3 == 0:
        m.append(f(s // 3, e))
    return sum(m)


print(f(30, 1))
