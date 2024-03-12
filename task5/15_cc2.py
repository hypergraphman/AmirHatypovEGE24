def f(n):
    s1 = bin(n)[2:]
    if s1.count('1') % 2 == 0:
        s2 = s1[1:].lstrip('0')
        if s2 == '':
            s2 = 0
    else:
        s2 = '1' + s1 + '00'
    if s2.count('1') % 2 == 0:
        s3 = s2[1:].lstrip('0')
        if s3 == '':
            s3 = 0
    else:
        s3 = '1' + s2 + '00'
    return int(s3, 2)
print(f(5))


for i in range(1,1000):
    if f(i) > 100:
        print(i)
        break