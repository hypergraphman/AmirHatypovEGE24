from itertools import permutations

words =[''.join(word)for word in permutations('ПЕРЕВЫБОРЫ', r=10)]
k = set()
for word in words:
    t = word.replace('П','1').replace('Е','0').replace('Р','1').replace('Е','0').replace('В','1').replace('Ы','0').replace('Б','1').replace('О','0').replace('Р','1').replace('Ы','0')
    if '00' not in t and '11' not in t:
        k.add(word)
print(len(k))