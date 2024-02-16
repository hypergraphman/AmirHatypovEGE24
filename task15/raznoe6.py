# for n in range(-50, 54):
#     k = 0
#     for x in range(-100, 100):
#         if ((25 <= x <= 40) <= (37 <= x <= 50)) and ((not (n <= x <= 54)) <= (37 <= x <= 50)):
#             k += 1
#     if k > 25:
#         print(n)


for n in range(-50, 54):
    if sum([((25 <= x <= 40) <= (37 <= x <= 50)) and ((not (n <= x <= 54)) <= (37 <= x <= 50)) for x in range(-100, 100)]) > 25:
        print(n)