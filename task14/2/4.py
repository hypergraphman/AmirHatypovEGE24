for x in range(24):
    for y in range(24):
        a = 3 * 24 ** 3 + x * 24 ** 2 + y * 24 ** 1 + 3 * 24 ** 0
        b = 1 * 24 ** 3 + y * 24 ** 2 + 3 * 24 ** 1 + 1 * 24 ** 0
        s = a + b
        if s % 5 == 0:
            print(x, y, s // 5)