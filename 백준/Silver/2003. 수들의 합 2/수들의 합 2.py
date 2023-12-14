import sys

n, m = map(int, sys.stdin.readline().strip().split())
a = [0] + list(map(int, sys.stdin.readline().strip().split()))

left, right, cnt = 0, 1, 0
for i in range(n):
    a[i+1] += a[i]

while left <= right <= n:
    if a[right]-a[left] < m: right += 1
    elif a[right]-a[left] > m: left += 1
    else: cnt += 1; left += 1; right += 1

print(cnt)