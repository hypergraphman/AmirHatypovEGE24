from itertools import product

words = [''.join(word) for word in product('ИЛЬДАР', repeat=5)]
k = 0
for word in words:
    if word.count('И') >= 1 and word[0] != 'Ь':
        k += 1
print(k)