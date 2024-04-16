from itertools import permutations

words = [''.join(word) for word in permutations('эмиль', r=5)]
k = set()
for word in words:
    if word[0] != 'ь' and 'иэ' not in word:
        k.add(word)
print(len(k))