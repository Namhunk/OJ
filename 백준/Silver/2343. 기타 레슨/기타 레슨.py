import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

def check(mid):
    SUM = 0
    cnt = 1
    for i in arr:
        if i > mid: return True
        if SUM + i <= mid: SUM += i
        else: cnt += 1; SUM = i
    
    return True if cnt > m else False

ans = float('inf')
low, high = 1, int(1e9)
while low <= high:
    mid = (low + high) // 2

    if check(mid): low = mid + 1
    else: high = mid - 1; ans = min(ans, mid)

print(ans)