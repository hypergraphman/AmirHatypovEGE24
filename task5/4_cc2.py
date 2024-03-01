def f(n):
    s1 = bin(n)[2:].rjust(8, '0')
    t = ''
    for c in s1:
        if c == '1':
            t += '0'
        else:
            t += '1'
    return int(t, 2)


for i in range(1, 1000):
    if f(i) - i == 131:
        print(i)


