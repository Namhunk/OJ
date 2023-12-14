from collections import deque
import sys

n, k, b = map(int, sys.stdin.readline().strip().split())

cnt = [0]*(n+1)
for _ in range(b):
    num = int(sys.stdin.readline().strip())
    cnt[num] = 1

for i in range(1, n+1):
    cnt[i] += cnt[i-1]

ans = float('inf')
for i in range(k, n+1):
    ans = min(ans, cnt[i] - cnt[i-k])

print(ans)