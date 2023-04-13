from itertools import permutations

words = permutations('ВУАЛЬ', r=5)
res = set()
for w in words:
    word = ''.join(w)
    if word[0] != 'Ь' and 'ЬУ' not in word and 'ЬА' not in word:
        res.add(word)
print(len(res))
