import sys
input = sys.stdin.readline

# N이 주어질때 길이가 N이면서 0부터 9까지 숫자가 모두 등장하는 계단 수가 총 몇 개 있는지 구하기(0으로 시작하는건 계단 수 x)
# 정답을 1e9로 나눈 나머지 출력

N = int(input().strip()) # 1 <= N <= 100
mod = int(1e9)
MAX = 10 # 0 ~ 9
BIT = 1 << MAX # 0 ~ 9 번호의 숫자 10개의 숫자가 모두 사용될라면 1023의 위치에 저장되어야 함

arr = [[[0]*BIT for _  in range(MAX)] for _ in range(N+1)]
for i in range(1, MAX): 
    arr[1][i][1 << i] = 1

for i in range(1, N):
    for j in range(MAX):
        for k in range(BIT):
            if j > 0:
                NEXT = k | 1 << (j-1)
                arr[i+1][j-1][NEXT] += arr[i][j][k]
                arr[i+1][j-1][NEXT] %= mod

            if j < 9:
                NEXT = k | 1 << (j+1)
                arr[i+1][j+1][NEXT] += arr[i][j][k]
                arr[i+1][j+1][NEXT] %= mod

ans = 0
for i in range(MAX):
    ans += arr[N][i][BIT-1]
    ans %= mod

print(ans)
