from itertools import product

words = [''.join(word) for word in product(sorted('МАОУЛИЦЕЙ', reverse=True), repeat=6)]
print(words[:10])
for i, word in enumerate(words, start=1):
    if word == 'УМЕЛЕЦ':
        print(i)