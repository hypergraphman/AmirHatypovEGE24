for a in range(1,1000):
    if all((60 >= x) and (20 >= y) or (2 * y + 5 * x > a) for x in range(1,1000) for y in range(1,1000)):
        print(a)
