import sys

l, p = map(int, sys.stdin.readline().strip().split())
pp = list(map(int, sys.stdin.readline().strip().split()))

rs = pp
for i in range(len(pp)):
    rs[i] = pp[i] - (l*p)

print(*rs)