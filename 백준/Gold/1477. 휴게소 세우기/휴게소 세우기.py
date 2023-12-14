import sys

n, m, l = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split())) + [l] + [0]
arr =sorted(arr)

ans = 0
low, high = 1, l-1
while low <= high:
    mid = (low + high) // 2
    cnt = 0

    for i in range(1, n+2):
        if arr[i] - arr[i-1] > mid: cnt += (arr[i] - arr[i-1] - 1) // mid

    if cnt > m: low = mid + 1
    else: high = mid - 1; ans = mid
print(ans)