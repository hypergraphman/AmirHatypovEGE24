from re import fullmatch

for x in range(157 * 4, 10**10, 157 * 10):
    if fullmatch(r'1[13579]*3456[02468]8', str(x)):
        print(x, x // 157, sep='*', end='-')
