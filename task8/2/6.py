from itertools import product

words = [''.join(word) for word in product('ДИЛЯРА', repeat=6)]
k = 0
for word in words:
    if word.count('И') <= 1 and word.count('Д') == 1 and word.count('Р') == 1:
        k += 1
print(k)