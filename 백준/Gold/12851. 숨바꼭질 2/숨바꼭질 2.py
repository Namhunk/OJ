from collections import deque
import sys

n, k = map(int, sys.stdin.readline().strip().split())
arr = [True]*(10**5+1)

que = deque([n])
time = 0
cnt = 0

while que:
    visited = set()
    for _ in range(len(que)):
        idx = que.popleft()
        if idx == k: cnt += 1

        if not arr[idx]: continue
        visited.add(idx)

        for i in [-1, 1, idx]:
            if 0 <= idx+i <= 10**5:
                que.append(idx+i)
    
    for i in visited:
        arr[i] = False

    if not arr[k]: break
    time += 1


print(time)
print(cnt)

"""

"""