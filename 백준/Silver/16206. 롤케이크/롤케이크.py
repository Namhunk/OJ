import sys

n, m = map(int, sys.stdin.readline().strip().split())
c = list(map(int, sys.stdin.readline().strip().split()))
c.sort()

r = 0

for i in range(n):
    if c[i] % 10 == 0:
        if c[i]//10 - 1 <= m:
            r += c[i]//10
            m -= (c[i]//10-1)
        
        elif c[i]//10 - 1 > m:
            r += m
            m = 0

for i in range(n):
    if m < 0:
        break
    if c[i] % 10 != 0:
        if c[i]//10 <= m:
            r += c[i]//10
            m -= (c[i]//10)
        elif c[i]//10 > m:
            r += m
            m = 0

print(r)