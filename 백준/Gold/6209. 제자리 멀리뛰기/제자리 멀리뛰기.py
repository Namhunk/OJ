import sys

d, n, m = map(int, sys.stdin.readline().strip().split())
arr = sorted(list(int(sys.stdin.readline().strip()) for _ in range(n))) + [d]

low, high = 0, int(1e9)
while low < high:
    mid = (low + high) // 2

    cnt = 0
    prev = 0

    for i in range(n+1):
        if arr[i] - prev > mid: prev = arr[i]
        else: cnt += 1
    
    if cnt > m: high = mid
    else: low = mid + 1

print(high)
