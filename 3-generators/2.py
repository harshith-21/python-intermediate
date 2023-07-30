def infinite_sequence():
    res = 1
    while True:
        yield res
        res += 1

sq = infinite_sequence()

for i in range(5):
    print(next(sq))