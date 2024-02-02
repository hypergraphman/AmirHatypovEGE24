for a in range(1, 1000):
    if all((x <= a) and (a > y) or (x + 7 * y != 50) for x in range(1,1000) for y in range(1, 1000)):
        print(a)
        break