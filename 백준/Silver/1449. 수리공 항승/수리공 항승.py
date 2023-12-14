import sys

n, l = map(int, sys.stdin.readline().strip().split())
x = list(map(int, sys.stdin.readline().strip().split()))
x.sort()

s = x[0]
r = 1

for i in x[1:]:
    if i in range(s, s+l):
        continue
    else:
        s = i
        r += 1

print(r)