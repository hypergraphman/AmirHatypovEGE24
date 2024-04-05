from itertools import product

words = [''.join(word) for word in product(sorted('КЕГЭАИТОВ'), repeat=6)]
c = 0
for i, word in enumerate(words, start=1):
    if i % 2 == 0 and word[0] != 'Т' and word.count('Е') == 2:
        c += 1
print(c)