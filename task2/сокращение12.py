for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(a or not (a or b) or not a and b)
            f2 = 1
            print(f, f2)
