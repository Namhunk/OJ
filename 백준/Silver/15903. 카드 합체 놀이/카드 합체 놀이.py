import sys

n, m = map(int, sys.stdin.readline().strip().split())
s = list(map(int, sys.stdin.readline().strip().split()))
s.sort()

for i in range(m):
    s[0] = s[1] = s[0] + s[1]
    s.sort()

print(sum(s))