for x in range( 16):
    a = x * 16 ** 7 + 1 * 16 ** 6 + 3 * 16 ** 5 + 1 * 16 ** 4 + x * 16 ** 3 + 1 * 16 ** 2 + 3 * 16 ** 1 + 1 * 16 ** 0
    b = 1 * 16 ** 6 + 4 * 16 ** 3 + x * 16 ** 0
    s = a + b
    if s % 15 == 0:
        print(x, s // 15)