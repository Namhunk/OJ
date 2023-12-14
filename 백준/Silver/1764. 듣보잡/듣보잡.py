import sys

n, m = map(int, sys.stdin.readline().strip().split())

nlist = set(sys.stdin.readline().strip() for _ in range(n))
mlist = set(sys.stdin.readline().strip() for _ in range(m))

s = sorted(list(nlist & mlist))

print(len(s))
for i in s:
    print(i)