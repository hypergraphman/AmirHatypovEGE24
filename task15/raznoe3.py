mn = float('inf')
for s in range(-100, 100):
    for e in range(s + 1, 100):
        if all(((s <= x <= e) <= (x * x <= 100)) and ((x * x <= 64) <= (s <= x <= e)) for x in range(-100, 100)):
            print(e - s, s, e)
            if e - s < mn:
                mn = e - s
print(mn)