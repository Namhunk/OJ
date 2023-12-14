import sys, math

n, k = map(int, sys.stdin.readline().strip().split())

rs = [0]
for i in range(1, n+1):
    if n % i == 0: rs.append(i)

if len(rs) <= k: print(0)
else: print(rs[k])