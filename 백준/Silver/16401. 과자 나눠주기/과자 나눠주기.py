import sys

m, n = map(int, sys.stdin.readline().strip().split())
l = sorted(list(map(int, sys.stdin.readline().strip().split())))

low, high = 1, l[n-1]
ans = 0
while low <= high:
    cnt = 0
    mid = (low + high) // 2

    for idx in range(n-1, -1, -1):
        if not l[idx] // mid: break
        cnt += l[idx] // mid
    
    if cnt >= m: low = mid + 1; ans = max(ans, mid)
    else: high = mid - 1

print(ans)