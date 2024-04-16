from itertools import product
k = 0
for n in product('01234567', repeat=5):
    t = ''.join(n)
    if t[0] != '0' and t.count('6') == 2 and '61' not in t and '63' not in t and '65' not in t and '67' not in t and '16' not in t and '36' not in t and '56' not in t and '76' not in t:
        k += 1
print(k)