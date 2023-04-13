from itertools import permutations

words = permutations('ЛЕБНЫЙМЯКИШ', r=6)
res = set()
for w in words:
    word = ''.join(w)
    template = word.replace('Л', '.').replace('Б', '.').replace('Н', '.').replace('Й', '.').replace('М', '.').replace('К', '.').replace('Ш', '.')
    if '..' not in template and word[0] in 'ЕЫЯИ' and word[2] in 'БЫКИШ':
        res.add(word)
print(len(res))