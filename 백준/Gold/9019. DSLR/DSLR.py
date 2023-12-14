import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    visited = [0] * 10000
    visited[a] = 1

    que = deque([(a, "")])
    while que:
        num, cmd = que.popleft()

        if num == b: ans = cmd; break
        else:
            d = (num * 2) % 10000
            s = (9999 if num-1 < 0 else num-1)
            l = ((num % 1000)*10 + (num // 1000))
            r = ((num % 10)*1000 + (num // 10))

            if not visited[d]: visited[d] = 1; que.append((d, cmd+"D"))
            if not visited[s]: visited[s] = 1; que.append((s, cmd+"S"))
            if not visited[l]: visited[l] = 1; que.append((l, cmd+"L"))
            if not visited[r]: visited[r] = 1; que.append((r, cmd+"R"))
    
    print(ans)