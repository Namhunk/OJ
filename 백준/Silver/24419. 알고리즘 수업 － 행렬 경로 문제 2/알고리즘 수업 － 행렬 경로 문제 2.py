import sys

n = int(sys.stdin.readline().strip())
m = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
arr = [[1 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

s = 0
for i in arr:
    s += sum(i)

print((s+1) % (10**9+7), (n**2) % (10**9+7))