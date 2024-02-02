for a in range(1, 100):
    if all(((not(x % a == 0) and (x % 180 == 0)) <= (x % 130 == 0)) for x in range(1, 10000)):
        print(a)