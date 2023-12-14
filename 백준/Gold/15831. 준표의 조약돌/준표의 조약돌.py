import sys

n, b, w = map(int, sys.stdin.readline().strip().split())
arr = list(sys.stdin.readline().strip())

cnt = {'W': 0, "B": 0}
left, ans = 0, 0
for right in range(n):
    cnt[arr[right]] += 1

    while cnt['B'] > b:
        cnt[arr[left]] -= 1
        left += 1
    
    if cnt['W'] >= w: ans = max(ans, right - (left - 1))

print(ans)
