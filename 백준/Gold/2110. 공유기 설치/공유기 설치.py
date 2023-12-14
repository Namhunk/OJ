import sys

n, c = map(int, sys.stdin.readline().strip().split())
arr = sorted(list(int(sys.stdin.readline().strip()) for _ in range(n)))

ans = 0
low, high = 0, int(1e9)
while low <= high:
    mid = (low + high) // 2

    prev = arr[0]
    cnt = 0

    for i in range(n):
        if arr[i] - prev >= mid: cnt += 1; prev = arr[i]
    
    if cnt < c-1: high = mid - 1
    else: low = mid + 1; ans = max(ans, mid)

print(ans)