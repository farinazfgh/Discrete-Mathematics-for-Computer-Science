n = 10
count = 0

for i in range(n):
    print("i:", i)
    for j in range(n):
        print("j:", j)
        for k in range(n):
            print("k:", k)
            if i < j and j < k:
                count += 1
                print("count:", count)

print(count)
