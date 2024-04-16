from itertools import product

words = [''.join(word) for word in product('БИЛств', repeat=5)]
k = 0
for word in words:
    if word.count('Б') + word.count('Л') == word.count('с') + word.count('т') + word.count('в'):
        k += 1
print(k)