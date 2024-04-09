from itertools import product

words = [''.join(word) for word in product('ЭЛИНА', repeat=5)]
k = 0
for word in words:
    t = word.replace('Э', '0').replace('Л', '1').replace('И', '0').replace('Н', '1').replace('А', '0')
    if '00' not in t and '11' not in t:
        k += 1
print(k)
