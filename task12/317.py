for m in range(0, 1000):
    s = '>' + '1' * 17 + '2' * 34 + '3' * m
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '1>', 1)
    sm = 0
    for char in s[:-1]:
        sm = sm + int(char)
    k = 0
    for i in range(2, sm // 2 + 1):
        if sm % i == 0:
            k = k + 1
    if k == 3:
        print(m)