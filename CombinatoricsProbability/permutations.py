from itertools import permutations

for p in permutations("abcd", 2):
    print("".join(p))
