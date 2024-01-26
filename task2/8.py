print('w z y x f')
for w in 0, 1:
    for z in 0, 1:
        for y in 0,1:
            for x in 0,1:
                f = int((w <= z) and (y <= w) or ((w or y) == x))
                if not f:
                    print(w,z,y,x,f)