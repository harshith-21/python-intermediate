import sys


def mygenerator(n):
    for x in range(n):
        yield x**3

values = mygenerator(1000000)

# print(next(values))
# print(next(values))
# print(next(values))

# print(next(values))
# print(next(values))
# print(next(values))

# print(next(values))
# print(next(values))
# print(next(values))

# print(next(values))
# print(next(values))
# print(next(values))

# for x in values:
#     print(x)


print(sys.getsizeof(values))

