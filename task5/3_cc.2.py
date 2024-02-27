def f(n):
    s1 = bin(n)[2:]
    s2 = s1[:-1]
    if n % 2 == 0:
        s3 = s2 + '01'
    else:
        s3 = s2 + '10'
    return int(s3, 2)


for i in range(1, 2025):
    if f(i) == 2025:
        print(i)
