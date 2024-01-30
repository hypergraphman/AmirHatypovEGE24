for a in range(1, 1000):
    if all((x % a == 0) or ((x % 35 == 0) <= (x % 49 == 0)) for x in range(1, 100000)):
        print(a)