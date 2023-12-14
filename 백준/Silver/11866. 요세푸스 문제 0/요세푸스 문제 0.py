import queue
import sys
N, K = map(int, sys.stdin.readline().strip().split())
que = queue.Queue(maxsize=N)
for i in range(1, N+1):
    que.put(i)
print('<',end='')
while que.qsize() != 0:
    for _ in range(K-1):
        que.put(que.get())
    if que.qsize() == 1: print(f'{que.get()}',end='')
    else: print(f'{que.get()}, ',end='')
print('>')