for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(not (a or not b) or not c)
            f2 = int(not a and b or not c)
            print(f, f2)
