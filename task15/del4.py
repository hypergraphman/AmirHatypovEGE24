for a in range(1, 1000):
    if all((x % a == 0) <= ((x % 34 == 0) and (x % 10 == 0)) for x in range(1, 1000)):
        print(a)
        break