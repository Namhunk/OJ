import sys, heapq

arr = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    cmd = int(sys.stdin.readline().strip())

    if not cmd: print(-heapq.heappop(arr) if arr else 0)
    else:
        heapq.heappush(arr, -cmd)