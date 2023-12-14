import sys, heapq

N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline().strip())

    if not x: print(heapq.heappop(arr)[1] if arr else 0)
    else: heapq.heappush(arr, (abs(x), x))
