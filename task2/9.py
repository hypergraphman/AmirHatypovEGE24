print('w z y x f')
for w in 0, 1:
    for z in 0, 1:
        for y in 0,1:
            for x in 0,1:
                f = int(((x <= z) == (y <= w)) or y and z)
                if not f:
                    print(w,z,y,x,f)