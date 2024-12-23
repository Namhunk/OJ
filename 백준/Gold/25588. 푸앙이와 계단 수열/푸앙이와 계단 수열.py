import sys
input = sys.stdin.readline

# 주어진 수열을 빈 수열로 만들기 위한 최소 연산 횟수를 출력하시오

# 푸앙이는 1 이상 9 이하의 양의 정수로 이루어진 길이가 N인 수열 A[1], A[2], ..., A[N]을 가지고 있으며 다음과 같은 연산을 할 수 있다
# 1. 수열의 왼쪽, 혹은 오른쪽에서부터 원소를 최대 3개 삭제한다
# 2. 수열의 왼쪽, 혹은 오른쪽에서부터 길이가 K인 계단 수열을 삭제한다
# 계단 수열이란 수열의 인접한 모든 원소의 차가 1인 수열이다
# 푸앙이는 여러 연산을 통해 자신이 가지고 있는 수열을 지우려 한다. 주어진 수열을 원소가 존재하지 않는 빈 수열로
# 만드는 데 필요한 연산의 최소 횟수를 구하시오

# 첫 번째 줄에 N (3 <= N <= 100,000), K (1 <= K <= N) 가 공백으로 구분되어 주어진다
N, K = map(int, input().strip().split())

# 두 번째 줄에 수열 A[1], A[2], ..., A[N]이 공백으로 구분되어 주어진다 (1 <= A[i] <= 9)
A = list(map(int, input().strip().split()))
rev_A = A[::-1] # A를 뒤집음
# 계단 수열 확인
left = [0]*N # 왼쪽부터
right = [0]*N # 오른쪽 부터

l_cnt = 0 # 왼쪽 시작 계단 수열 길이
r_cnt = 0 # 오른쪽 시작 계단 수열 길이

for i in range(1, N):
    # 왼쪽 부터 두 숫자의 차이가 1이면 계단 수열
    if abs(A[i] - A[i-1]) == 1:
        l_cnt += 1
    else:
        l_cnt = 0

    # 오른쪽 부터 두 숫자의 차이가 1이면 계단 수열
    if abs(rev_A[i] - rev_A[i-1]) == 1:
        r_cnt += 1
    else:
        r_cnt = 0

    # i-(K-1) 위치 부터 i 위치까지 계단 수열 이면 배열의 값을 1로
    if l_cnt >= K-1:
        left[i] = 1

    if r_cnt >= K-1:
        right[i] = 1

dp = [[float('inf')]*(N+1) for _ in range(2)] # 0 왼쪽, 1 오른쪽
dp[0][0] = 0
dp[1][0] = 0

for i in range(1, N+1):
    for j in range(1, 4): # 최대 3개를 지움
        if i-j >= 0: # 현재 위치 기준 최대 3번째 전까지 연산 횟수 중 가장 작은 연산
            dp[0][i] = min(dp[0][i], dp[0][i-j]+1)
            dp[1][i] = min(dp[1][i], dp[1][i-j]+1)

    if K <= i: # 시작점 부터 i의 길이가 K 이상이면 계단 수열인지 확인
        if left[i-1]:
            dp[0][i] = min(dp[0][i], dp[0][i-K] + 1)

        if right[i-1]:
            dp[1][i] = min(dp[1][i], dp[1][i-K] + 1)

ans = float('inf') # 결과
for i in range(N+1):
    # 왼쪽의 i개를 지웠을 때의 연산 횟수 + 오른쪽의 N-i개를 지웠을 때의 연산 횟수
    if dp[0][i] + dp[1][N-i] < ans:
        ans = dp[0][i] + dp[1][N-i]

print(ans)
