from collections import deque
import sys

n, k = map(int, sys.stdin.readline().strip().split())
visited = [True]*(10**5+1)
que = deque([(n, 0)])
visited[n] = False
if n == k: print(0); exit()
while que:
    idx, t = que.popleft()
    for i in [-1, 1, idx]:
        if 0 <= idx+i <= 10**5 and visited[idx+i]:
            if idx+i == k: print(t+1); exit()
            visited[idx+i] = False
            que.append((idx+i, t+1))
