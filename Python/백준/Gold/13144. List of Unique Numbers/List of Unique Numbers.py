import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

cnt = {}
left, ans = 0, 0
for right in range(n):
    cnt[arr[right]] = cnt.get(arr[right], 0) + 1

    while cnt[arr[right]] > 1:
        cnt[arr[left]] -= 1
        left += 1
    
    ans += (right - left + 1)

print(ans)