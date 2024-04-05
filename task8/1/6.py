from itertools import product

words = [''.join(word) for word in product(sorted('ЕГКЭАИТОВРУ'), repeat=6)]
for i, word in enumerate(words, start=1):
    if i % 2 != 0 and word[0] != 'У' and word.count('К') == 2 and word.count('В') > 0:
        print(i)