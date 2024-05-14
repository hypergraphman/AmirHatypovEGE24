def f(s, c, m):
    if s > 131:
        return c % 2 != m % 2
    if s >= 99:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [
             f(s + 1, c + 1, m),
             f(s * 2, c + 1, m),
             f(s * 3, c + 1, m),
             ]
    if (c + 1) % 2 == m % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 99):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 4:
                print(s)
            break