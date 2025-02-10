import sys
input = sys.stdin.readline

# 첫째 줄에 문제의 정답을 출력, 첫째 줄에 R1행의 모습을 출력하고 이런 식으로 R2-R1+1개의 줄에 출력
# C1열 부터 C2열 까지 차례대로 흰색이면 숫자 '0' 검정이면 숫자 '1'을 출력, 숫자사이에 공백 x

# 7개의 정수 s, N, K, R1, R2, C1, C2
s, N, K, R1, R2, C1, C2 = map(int, input().strip().split())

size = N**s

def solve(size, x, y): # size = 평면의 크기, x, y 출력해야 하는 좌표 위치
    center = size//N
    if size == 1:
        return 0
    if center * (N-K)//2 <= x < center * (N+K)//2 and center * (N-K)//2 <= y < center * (N+K)//2:
        return 1
    x %= center
    y %= center

    return solve(size//N, x, y)

for i in range(R1, R2+1):
    for j in range(C1, C2+1):
        print(solve(size, i, j), end="")
    print()

