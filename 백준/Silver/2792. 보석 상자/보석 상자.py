import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [int(sys.stdin.readline().strip()) for _ in range(m)]

ans = float('inf')
low, high = 1, int(1e9)
while low <= high:
    cnt = 0
    mid = (low + high) // 2
    for i in arr:
        if i % mid: cnt += (i // mid + 1)
        else: cnt += (i // mid)
    
    if cnt > n: low = mid + 1 
    else: high = mid - 1; ans = min(ans, mid)

print(ans)