import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

ans = float('inf')
low, high = 0, int(1e12)
while low <= high:
    cnt = 0
    mid = (low + high) // 2

    for time in arr:
        cnt += (mid//time)
    
    if cnt >= m: high = mid - 1; ans = min(ans, mid)
    else: low = mid + 1

print(ans)