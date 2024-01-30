print('w x z y f')
for w in 0, 1:
    for x in 0, 1:
        for z in 0, 1:
            for y in 0, 1:
                f = int((z == w) == ((y and not z) <= (not x and w)))
                if f:
                    print(w, x, z, y, f)
