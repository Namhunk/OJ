import sys

r = 1
dl = []
for _ in range(int(sys.stdin.readline().strip())):
    a, l = map(int, sys.stdin.readline().strip().split())
    dl.append((a, l))

dl.sort()
ds = []
for i in dl:
    ds.append(i[0]+i[1])

for i in range(1, len(dl)):
    if ds[i-1] < dl[i][0]: r+=1

print(r)