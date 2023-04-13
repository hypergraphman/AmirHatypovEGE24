from itertools import product
words=product('ВЕСНА',repeat=3)
k=0
for w in words:
    word=''.join(w)
    if 'А' in word:
        k+=1
print(k)