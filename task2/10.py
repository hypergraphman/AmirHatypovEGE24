print('w z y x f')
for w in 0, 1:
    for z in 0, 1:
        for y in 0, 1:
            for x in 0, 1:
                f = int(((y <= x) == (x <= w)) and ((not x) <= z))
                if f:
                    print(w,z,y,x,f)