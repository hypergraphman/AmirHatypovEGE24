for x in range(25):
    for y in range(11):
        a = 7 * 25 ** 5 + y * 25 ** 4 + 2 * 25 ** 3 + 3 * 25 ** 2 + x * 25 ** 1 + 5 * 25 ** 0
        b = 6 * 11 ** 4 + 7 * 11 ** 3 + x * 11 ** 2 + 9 * 11 ** 1 + y * 11 ** 0
        s = a + b
        if s % 131 == 0:
            print(x, y, s // 131)