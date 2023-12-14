import sys

n, m = map(int, sys.stdin.readline().strip().split())
poketmon = {sys.stdin.readline().strip(): i for i in range(1, n+1)}
pk = list(poketmon.keys())

for _ in range(m):
    Q = sys.stdin.readline().strip()
    if Q.isalpha():print(poketmon[Q])
    else: print(pk[int(Q)-1])