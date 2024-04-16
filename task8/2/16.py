from itertools import permutations

words = [''.join(word) for word in permutations('РАВИЛЬ', r=6)]
k = set()
for word in words:
    if word[0] != 'Ь' and 'АЬ' not in word and 'ИЬ' not in word:
        k.add(word)
print(len(k))