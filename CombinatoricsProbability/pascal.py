C = dict()  # C ( [ n , k ] )   i s   equal  to  n  choose  k
for n in range(8):
    C[n, 0] = 1
    C[n, n] = 1
    for k in range(1, n):
        C[n, k] = C[n - 1, k - 1] + C[n - 1, k]
print(C[7, 4])
