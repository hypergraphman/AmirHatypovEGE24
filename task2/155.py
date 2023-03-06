print('x y z f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x <= (not z)) and ((not y) <= x)
            print(x, y, z, int(f))