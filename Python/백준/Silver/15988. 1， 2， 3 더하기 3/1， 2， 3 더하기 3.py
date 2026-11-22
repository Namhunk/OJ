import sys

t = int(sys.stdin.readline().strip())
arr = [0, 1, 2, 4] + [0] * (10**6-3)

for i in range(4, len(arr)):
    arr[i] = (arr[i-3] + arr[i-2] + arr[i-1]) % (10**9 + 9)

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(arr[n])
