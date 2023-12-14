import sys
from collections import deque

def bfs():
    que = deque([(1, 0)])
    while que:
        now, cnt = que.popleft()
        for i in range(1, 7):
            if arr[now+i] < 100:
                if visited[now+i]:
                    que.append((arr[now+i], cnt+1))
                    visited[now+i] = False
            else:
                return cnt+1
            
arr = [i for i in range(101)]
visited = [True]*101
n, m = map(int, sys.stdin.readline().strip().split())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[x] = y

for _ in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    arr[u] = v

print(bfs())