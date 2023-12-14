import sys
from collections import deque

n, l = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
que = deque()

al, cnt = 0, 0
for i in range(n):
    que.append(arr[i])
    al += arr[i]
    if len(que) > l: al -= que.popleft()

    if 129 <= al <= 138: cnt += 1

print(cnt)