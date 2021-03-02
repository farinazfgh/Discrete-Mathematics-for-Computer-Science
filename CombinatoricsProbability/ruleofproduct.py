from itertools import product

for p in product(['a', 'b', 'c'], ['x', 'y']):
    print("".join(p))
