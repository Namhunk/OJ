import sys

r, c, q = map(int, sys.stdin.readline().strip().split())
arr = [[0]*(c+1)] + [[0] + list(map(int, sys.stdin.readline().strip().split())) for _ in range(r)]

for i in range(1, r+1):
    for j in range(1, c+1):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().strip().split())
    area = arr[r2][c2] - arr[r2][c1-1] - arr[r1-1][c2] + arr[r1-1][c1-1] 
    print(area // ((r2-r1+1)*(c2-c1+1)))