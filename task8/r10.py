from itertools import permutations
words=permutations('КАПКАН',r=6)
res=set()
for w in words:
    word=''.join(w)
    if 'АА' not in word and 'КК' not in word:
        res.add(word)
print(len(res))