import sys
from collections import deque
N = int(sys.stdin.readline().strip())
que = deque(range(1, N+1))
while len(que) > 1:
    que.popleft()
    que.append(que.popleft())
card = que.popleft()
print(card)