def f(s, c, m):
    if s >= 221:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(s + 2, c + 1, m),
             f(s + 3, c + 1, m),
             f(s * 2, c + 1, m)]
    if (c + 1) % 2 == m % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 221):
    for m in range(1, 4):
        if f(s, 0, m):
            if m == 2:
                print(s)
            break