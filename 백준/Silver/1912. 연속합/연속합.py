import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n):
    arr[i] = max(arr[i-1] + arr[i], arr[i])

print(max(arr))