from itertools import product

words = [''.join(word) for word in product(sorted('АИТОВРУ'), repeat=5)]
# print(words[:10])
for i, word in enumerate(words, start=1):
    if word == 'ТОВАР':
        print(i)
