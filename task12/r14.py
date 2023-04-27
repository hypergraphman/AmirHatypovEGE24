for x in range(100):
    for y in range(27):
        for z in range(27):
            if 2 * x + 3 * y + 6 * z == 186 and y + z == 26:
                print(x + y + z + 2)