import sys

n, m = map(int, sys.stdin.readline().strip().split())
a = [[int(i) for i in sys.stdin.readline().strip()] for _ in range(n)]
b = [[int(i) for i in sys.stdin.readline().strip()] for _ in range(n)]

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            cnt += 1
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if a[x][y] == 1: a[x][y] = 0
                    else: a[x][y] = 1

print(cnt if a == b else -1)