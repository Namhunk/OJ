import sys

t = 0
m = 0
for _ in range(4):
    Out, In = map(int, sys.stdin.readline().strip().split())
    t -= Out
    t += In
    if t > 10**4: t -= (t-10**4)
    if t > m: m = t
print(m)