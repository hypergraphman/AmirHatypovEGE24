k = 0
for a in range(0, 3000):
    if all(((x > 10) <= (x * x * x + 3 * x >= a)) and ((y * y + 5 * y > a) <= (y >= 10)) for x in range(0, 100) for y in range(0,100)):
        k += 1
print(k)