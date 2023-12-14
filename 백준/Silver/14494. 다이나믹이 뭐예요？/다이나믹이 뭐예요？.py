import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [[1 for _ in range(m)] for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i-1][j-1]

print(arr[-1][-1] % (10**9 + 7))