import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

B_arr = [[0]*(m+1) for _ in range(n+1)] # (0, 0)이 B로 시작
W_arr = [[0]*(m+1) for _ in range(n+1)] # (0, 0)이 W로 시작

for i in range(n):
    for j in range(m):
        if (i+j) % 2:
            if arr[i][j] == 'B': B_arr[i+1][j+1] += 1
            else: W_arr[i+1][j+1] += 1
        else:
            if arr[i][j] == 'W': B_arr[i+1][j+1] += 1
            else: W_arr[i+1][j+1] += 1
for i in range(1, n+1):
    for j in range(1, m+1):
        B_arr[i][j] += B_arr[i-1][j] + B_arr[i][j-1] - B_arr[i-1][j-1]
        W_arr[i][j] += W_arr[i-1][j] + W_arr[i][j-1] - W_arr[i-1][j-1]

ans = float('inf')
for i in range(k, n+1):
    for j in range(k, m+1):
        b_cnt = B_arr[i][j] - B_arr[i-k][j] - B_arr[i][j-k] + B_arr[i-k][j-k]
        w_cnt = W_arr[i][j] - W_arr[i-k][j] - W_arr[i][j-k] + W_arr[i-k][j-k]

        ans = min(ans, b_cnt, w_cnt)

print(ans)