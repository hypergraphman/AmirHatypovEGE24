print('x y z f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = int((x or z) <= (y == z))
            if not f:
                print(x,y,z,f)