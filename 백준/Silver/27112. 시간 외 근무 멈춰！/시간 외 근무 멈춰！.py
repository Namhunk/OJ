import sys

n = int(sys.stdin.readline().strip())
dt = []
d = w = e = 0
re =  r = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    dt.append([a, b])

dt.sort()

for i in range(n):
    while d < dt[i][0]:
        if d % 7 < 5: w += 1
        e += 1; d += 1
    
    if w >= dt[i][1]: w -= dt[i][1]
    elif w + e >= dt[i][1]:
        r = dt[i][1] - w
        w = 0; e -= r; re += r
    else:
        re = -1
        break

print(re)