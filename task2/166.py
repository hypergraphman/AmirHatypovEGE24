print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not (x or not w or (y and not z)):
                    print(x, y, z, w)
