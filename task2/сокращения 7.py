for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f1 = int(((not a) or b) and (not c) and (c or a and (not b)))
            f2 = 0
            print(f1, f2)