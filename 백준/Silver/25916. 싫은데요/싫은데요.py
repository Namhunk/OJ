import sys

n, m = map(int, sys.stdin.readline().strip().split())
a = [0] + list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n+1):
    a[i] += a[i-1]

left, right, ans = 0, 0, 0

while right <= n:
    if a[right] - a[left] <= m:
        ans = max(ans, a[right] - a[left])
        right += 1
    else:
        left += 1

print(ans)
