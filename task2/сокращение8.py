for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int((not a) and (not c) or a and b or (not a) and c or a and (not b))
            f2 = 1
            print(f, f2)
