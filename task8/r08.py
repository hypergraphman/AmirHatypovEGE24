from itertools import permutations

words = permutations('УЛЕЙ', r=4)
res = set()
for w in words:
    word = ''.join(w)
    if word[0] != 'Й' and 'ЕУ' not in word:
        res.add(word)
print(len(res))