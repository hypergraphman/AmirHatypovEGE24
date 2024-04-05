from itertools import product

words = [''.join(word) for word in product(sorted('АРСЕНИЙ'), repeat=6)]
for i, word in enumerate(words, start=1):
    t = word.replace('А', '0').replace('Р', '1').replace('С', '1').replace('Е', '0').replace('Н', '1').replace('И', '0').replace('Й', '1')
    if i % 2 == 0 and word[0] not in 'РС' and '00' not in t and '11' not in t:
        print(i)