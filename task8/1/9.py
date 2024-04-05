from itertools import product

words = [''.join(word) for word in product(sorted('ЛАСТИК'), repeat=5)]
c = 0
for i, word in enumerate(words, start=1):
    t = word.replace('Л','1').replace('А','0').replace('С','1').replace('Т','1').replace('И','0').replace('К','1')
    if 'КАСКА' <= word and i <= 4045 and '00' not in t and '11' not in t:
        c += word.count('И')
print(c)