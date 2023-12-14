N = int(input())
min = 0
for i in range(N, 0, -1):
    a = []
    l = len(str(i))
    for j in range(l, 0, -1):
        a.append((i % (10 ** j)) // 10 ** (j - 1))
    if sum(a) + i == N:
        min = i

print(min)