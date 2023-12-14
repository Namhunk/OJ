import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

ans = float('inf')
low, high = 0, int(1e8)
while low <= high:
    mid = (low + high) // 2

    cnt = 1
    MIN = float('inf')
    MAX = 0

    temp = 0

    for i in range(n):
        MIN = min(MIN, arr[i])
        MAX = max(MAX, arr[i])

        if MAX - MIN >= mid: cnt += 1; MIN, MAX = arr[i], arr[i]
        else: temp = max(temp, MAX - MIN)

    if cnt <= m: high = mid - 1; ans = min(ans, temp)
    else: low = mid + 1

print(ans)
