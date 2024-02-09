for n in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        if ((not (70 <= x <= 90)) <= (15 <= x <= 50)) and ((not (20 <= x <= n)) <= (70 <= x <= 90)):
            k += 1
    if k > 35:
        print(n)
