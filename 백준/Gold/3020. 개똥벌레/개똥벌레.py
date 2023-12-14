import sys

n, h = map(int, sys.stdin.readline().strip().split())

arr = [0]*(h+1)

for i in range(1, n+1):
    k = int(sys.stdin.readline().strip())
    if i % 2: arr[h-k] += 1; arr[h] -= 1
    else: arr[0] += 1; arr[k] -= 1

for i in range(h):
    arr[i+1] += arr[i]

print(min(arr[: h]), arr[: h].count(min(arr[: h])))
