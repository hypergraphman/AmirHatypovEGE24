for a in range(1, 100):
    if all(((x <= 60) <= (x <= a)) and ((y * y <= a) <= (y <= 8)) for x in range(0, 100) for y in range(0, 100)):
        print(a)