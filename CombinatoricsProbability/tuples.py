from itertools import product

for p in product("ab", repeat=3):
    print("".join(p))
