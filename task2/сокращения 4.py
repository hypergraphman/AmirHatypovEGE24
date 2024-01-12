for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f1 = int(a or not a and b or not a and c)
            f2 = int(b or a or c)
            print(f1, f2)