for x in range(15):
    for y in range(17):
        a = 1 * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 ** 1 + 5 * 15 ** 0
        b = 6 * 17 ** 3 + 7 * 17 ** 2 + y * 17 ** 1 + 9 * 17 ** 0
        s = a + b
        if s % 131 == 0:
            print(x, y, s // 131)
