print('y x z f')
for y in 0, 1:
    for x in 0, 1:
        for z in 0, 1:
            f = int((y == x) or ((y or z) <= x))
            if not f:
                print(y,x,z,f)