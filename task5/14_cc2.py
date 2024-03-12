def f(n):
    s1 = bin(n)[2:]
    # print(s1)
    if s1.count('1') % 2 == 0:
        s2 = s1[1:].lstrip('0')
        if s2 == '':
            s2 = '0'
    else:
        s2 = s1.count('1') * '1' + '1'
    # print(s2)
    if s2.count('1') % 2 == 0:
        s3 = s2[1:].lstrip('0')
        if s3 == '':
            s3 = '0'
    else:
        s3 = s2.count('1') * '1' + '1'
    # print(s3)
    return int(s3, 2)


# print(f(5))
k = 0
for i in range(1, 1000 + 1):
    if f(i) == 7:
        k += 1
print(k)