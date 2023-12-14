import sys

n = int(sys.stdin.readline().strip())
p = []
t = [(0, 2**31-1)]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    p.append((a, b))

p.sort()

for i in p:
    if t[-1][0] <= i[0] < t[-1][1] and i[1] <= t[-1][1]:
        t[-1] = i
    elif t[-1][1] <= i[0]:
        t.append(i)

print(len(t))