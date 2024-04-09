from itertools import product

words1 = [''.join(word) for word in product('КРСТИНА', repeat=3)]
words2 = [''.join(word) for word in product('ЛИЯ', repeat=2)]
print(len(words1) * len(words2))