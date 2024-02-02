for a in range(201, 1000):
    if all((((x % a == 0) and (x % 45 == 0)) <= (x % 162 == 0)) for x in range(1, 10000000)):
        print(a)
        break