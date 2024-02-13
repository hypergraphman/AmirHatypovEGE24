mx = 0
for s in range(-100, 100):
    for e in range(-100, 100):
        if all(((x * x <= 20) <= (s <= x <= e)) and ((s <= x <= e) <= (x * x <= 144)) for x in range(-100, 100)):
            print(e - s, s, e)
            mx = max(mx, e - s)
print(mx)