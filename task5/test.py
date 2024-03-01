n = 12
s = bin(n)[2:].rjust(8, '0')
t = ''
for c in s:
    if c == '1':
        t += '0'
    else:
        t += '1'

t2 = ''
for c in s:
    t2 += '0' if c == '1' else '1'

t3 = ''.join('0' if c == '1' else '1' for c in s)

print(t)
print(t2)
print(t3)