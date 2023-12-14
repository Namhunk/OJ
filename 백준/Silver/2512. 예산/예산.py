import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())

low, high = 0, max(arr)
ans = 0

while low <= high:
    SUM = 0
    mid = (low + high) // 2

    for num in arr:
        SUM += min(mid, num)
    
    if SUM <= m: low = mid + 1; ans = mid
    else: high = mid - 1

print(ans)