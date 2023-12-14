import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

target = sum(arr)
ans = 0
temp = arr[0]

for i in range(1, n):
    temp += arr[i]
    ans = max(ans, (target - arr[0]) + (target - temp - arr[i]))

arr.reverse()
temp = arr[0]
for i in range(1, n):
    temp += arr[i]
    ans = max(ans, (target - arr[0]) + (target - temp - arr[i]))

for i in range(1, n):
    ans = max(ans, target - arr[0] - arr[n-1] + arr[i])

print(ans)