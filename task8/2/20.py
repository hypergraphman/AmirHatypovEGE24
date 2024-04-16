from itertools import permutations

words = [''.join(word) for word in permutations('АЛИНА', r=5)]
k = set()
for word in words:
    if 'АА' not in word:
        k.add(word)
print(len(k))