import sys

n = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().strip().split()))
p = list(map(int, sys.stdin.readline().strip().split()))

mi = [0]
for i in range(1, n-1):
    if p[mi[-1]] > p[i]: mi.append(i)

mi.append(n-1)
r = 0
for i in range(1, len(mi)):
    r += p[mi[i-1]]*sum(l[mi[i-1]:mi[i]])

print(r)