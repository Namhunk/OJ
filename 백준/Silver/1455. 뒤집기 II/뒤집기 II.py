import sys

n, m = map(int, sys.stdin.readline().strip().split())
r = 0
coin = [list(sys.stdin.readline().strip()) for _ in range(n)]

for a in range(n-1, -1, -1):
    for b in range(m-1, -1, -1):
        if coin[a][b] == '1':
            r += 1
            for i in range(a, -1, -1):
                for j in range(b, -1, -1):
                    if coin[i][j] == "1": coin[i][j] = "0"
                    else: coin[i][j] = "1"

print(r)