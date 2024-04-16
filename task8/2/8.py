from itertools import product

words = [''.join(word) for word in product('КАРИМ', repeat=5)]
k = 0
for word in words:
    if word.count('К') <= 2 and word.count('КА') + word.count('КИ') == word.count('К'):
        k += 1
print(k)
        