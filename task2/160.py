print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not ((x or not y or not z) and (x or not y or z) and (x or y or z)):
                print(x, y, z)
