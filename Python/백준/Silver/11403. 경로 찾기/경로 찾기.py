import sys
from collections import deque

N = int(sys.stdin.readline().strip())
G = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][k] and G[k][j]:
                G[i][j] = 1

for i in G:
    print(*i)