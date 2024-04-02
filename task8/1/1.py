from itertools import product

words = [''.join(word) for word in product(sorted('СНЕГУРОЧКА'), repeat=5)]
# print(words[:20])
k = 0
for word in words:
    if 'РУЧКА' <= word <= 'ЧУКЧА':
        k += 1
print(k)