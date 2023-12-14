import sys

n, m = map(int, sys.stdin.readline().strip().split())
t = list(int(sys.stdin.readline().strip()) for _ in range(n))

ans = float('inf')
low, high = 1, int(1e18)
while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for i in range(n):
        cnt += (mid // t[i])
    
    if cnt >= m: high = mid - 1; ans = min(ans, mid)
    else: low = mid + 1

print(ans)