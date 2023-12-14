import sys

n, s = map(int, sys.stdin.readline().strip().split())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n+1): arr[i] += arr[i-1]

ans = float('inf')
left, right = 0, 0
while right <= n:
    if arr[right] - arr[left] < s: right += 1
    else: ans = min(ans, right - left); left += 1

print(ans if ans != float('inf') else 0)