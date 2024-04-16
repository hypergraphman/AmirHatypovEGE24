from itertools import product
k = 0
for n in product('01234', repeat=5):
    t = ''.join(n)
    if t[0] != '0' and len(set(t)) == 4 and '11' not in t and '00' not in t and '22' not in t and '33' not in t and '44' not in t:
        k += 1
print(k)