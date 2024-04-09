from itertools import product

words = [''.join(word) for word in product('ЛИЦЕЙ', repeat=4)]
print(len(words))