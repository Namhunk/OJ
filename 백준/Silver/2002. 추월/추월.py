import sys

n = int(sys.stdin.readline().strip())
dg, ys = {}, []
for i in range(1, n+1):
    number = sys.stdin.readline().strip()
    dg[number] = i
for i in range(1, n+1):
    number = sys.stdin.readline().strip()
    ys.append(dg[number])

MIN, cnt = float('inf'), 0
for i in range(n-1, -1, -1):
    if ys[i] < MIN: MIN = ys[i]
    else: cnt += 1

print(cnt)