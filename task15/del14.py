for a in range(111, 10000):
    if all((x % a == 0) <= (x % 54 == 0) or (x % 130 == 0) for x in range(1,10000)):
        print(a)
        break