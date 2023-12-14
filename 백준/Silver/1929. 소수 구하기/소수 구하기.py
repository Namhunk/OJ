import sys

M, N = map(int, sys.stdin.readline().strip().split())
sosu = set(i for i in range(2, 1000001))
for i in range(2, 1000001):
    n = set((i*x) for x in range(2, 1000000 // i + 1))
    sosu -= n
for i in range(M, N+1):
    if i in sosu:
        print(i)
