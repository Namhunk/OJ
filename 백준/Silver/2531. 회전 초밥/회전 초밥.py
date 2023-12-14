import sys

n, d, k, c = map(int, sys.stdin.readline().strip().split())
cnt = [0]*(d+1)
cnt[c] += 1

arr = [0]*(2*n+1)
left, ans, current = 1, 0, 1

for right in range(1, n+k+1):
    if right <= n:
        sushi = int(sys.stdin.readline().strip())
        arr[right] = sushi
        arr[n+right] = sushi
    
    if not cnt[arr[right]]: current += 1
    cnt[arr[right]] += 1

    ans = max(ans, current)

    if right >= k:
        cnt[arr[left]] -= 1
        if not cnt[arr[left]]: current -= 1
        left += 1

print(ans)