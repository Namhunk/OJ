import sys

n, k = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
check = [0] * (10**5 + 1)

ans, current = 0, 0
left = 0

for right in range(n):
    check[a[right]] += 1

    while check[a[right]] > k:
        if ans < current:
            ans = current
        
        check[a[left]] -= 1
        left += 1
        current -= 1
    
    current += 1

if ans < current: ans = current
print(ans)