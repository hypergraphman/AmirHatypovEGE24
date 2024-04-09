from itertools import product

words = [''.join(word) for word in product('КАМИЛЬ', repeat=6)]
k = 0
for word in words:
    if word.count('М') == 1 and word[0] != 'Ь':
        k += 1
print(k)