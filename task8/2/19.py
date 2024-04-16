from itertools import permutations

words = [''.join(word) for word in permutations('АРСЕНИЙ', r=5)]
k = set()
for word in words:
    if word[0] != 'Й' and 'РАЙ' not in word:
        k.add(word)
print(len(k))