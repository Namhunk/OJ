import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = sorted(list(int(sys.stdin.readline().strip()) for _ in range(n)))

ans = 2*1e9

left, right = 0, 0
while right < n:
    if left < right:
        if arr[right] - arr[left] < m: right += 1
        else: ans = min(ans, arr[right] - arr[left]); left += 1
    else:
        right += 1
        
print(ans)