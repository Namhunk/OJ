import sys

n, k = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

ans, pSum, cnt = 0, 0, { 0: 1 }
for i in range(n):
    pSum += arr[i]
    if pSum - k in cnt: ans += cnt[pSum - k]
    if pSum in cnt: cnt[pSum] += 1
    else: cnt[pSum] = 1

print(ans)
