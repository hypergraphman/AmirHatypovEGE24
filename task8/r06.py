from itertools import product
words=product ('СЛОН',repeat=5)
k=0
for w in words:
    word=''.join(w)
    if word.count('С')==1:
        k+=1
print(k)