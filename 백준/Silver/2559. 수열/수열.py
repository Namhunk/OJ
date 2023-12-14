import sys

n, k = map(int, sys.stdin.readline().strip().split())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n+1):
    arr[i] += arr[i-1]

left, right = 0, k
ans = arr[right] - arr[left]

while right <= n:
    ans = max(ans, arr[right] - arr[left])
    left += 1; right += 1
    
print(ans)
