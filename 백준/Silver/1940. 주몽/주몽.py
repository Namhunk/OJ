import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

left, right, cnt = 0, n-1, 0
while left < right:
    if arr[left] + arr[right] < m: left += 1
    elif arr[left] + arr[right] > m: right -= 1
    else: cnt += 1; left += 1; right -= 1

print(cnt)