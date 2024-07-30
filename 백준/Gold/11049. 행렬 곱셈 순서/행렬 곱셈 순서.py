import sys
input = sys.stdin.readline

# 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다, 정답은 2^31-1보다 작거나 가은 자연수

N = int(input().strip()) # 행렬의 개수 N(1 <= N <= 500)
arr = [list(map(int, input().strip().split())) for _ in range(N)] # N개의 행렬의 크기 r, c
# r x c의 행렬
# 입력으로 주어진 행렬의 순서를 바꾸면 안됨
# 항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어짐

# dp[첫 행렬 위치][k] + dp[k+1][마지막 행렬 위치] + (arr[첫 행렬 위치][0] * arr[k][1] * arr[마지막 행렬 위치][1])

dp = [[0]*N for _ in range(N)]

for d in range(1, N):
    for i in range(N-d):
        j = i + d
        if d == 1:
            dp[i][j] = arr[i][0] * arr[j][0] * arr[j][1]
            continue

        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+arr[i][0]*arr[k][1]*arr[j][1])
print(dp[0][N-1])

