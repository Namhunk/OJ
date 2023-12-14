import sys

n, x = map(int, sys.stdin.readline().strip().split())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n+1):
    arr[i] += arr[i-1]
ans = [0]*(n-x+1)
for i in range(n-x+1):
    ans[i] = (arr[i+x] - arr[i])

if not max(ans): print('SAD')
else:
    print(max(ans))
    print(ans.count(max(ans)))