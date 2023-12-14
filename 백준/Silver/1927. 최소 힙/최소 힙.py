import sys, heapq

arr = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    X = int(sys.stdin.readline().strip())
    if not X:
        if not len(arr): print(0)
        else: print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, X)