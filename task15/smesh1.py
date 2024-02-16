for a in range(1, 1000):
    if all(((x % 8 == 0) <= (not (x % 6 == 0))) or (x + 2 * a > 100) for x in range(1, 1000)):
        print(a)
        break