import sys
# 1.출력은 r1행부터 r2행까지 차례대로 출력
# 2.각 원소는 공백으로 구분
# 3.모든 행은 같은 길이를 가져야함
# 4.공백의 길이는 최소
# 5.모든 숫자의 길이(앞에 붙는 공백을 포함)는 같아야 함
# 6.수의 길이가 가장 긴 수보다 작다면, 왼쪽에서부터 공백을 삽입해 길이를 맞춘다.

# r2 - r1 + 1 개의 줄에 소용돌이를 예쁘게 출력
r1, c1, r2, c2 = map(int, sys.stdin.readline().strip().split())
N, M = (r2-r1+1), (c2-c1+1)

arr = [[0]*M for _ in range(N)]
MAX = 0
# (0, 0) 을 지나는 대각선을 기준으로 4개의 구역으로 나눔
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        # (0, 0) 기준 위쪽 삼각형 범위
        if i < 0 and abs(i) >= abs(j):
            arr[i-r1][j-c1] = str((2*i)**2+1-(j-i))
        # (0, 0) 기준 아래쪽 삼각형 범위
        elif i > 0 and abs(i) >= abs(j):
            arr[i-r1][j-c1] = str((2*i+1)**2-(i-j))
        # (0, 0) 기준 왼쪽 삼각형 범위
        elif j < 0 and abs(j) >= abs(i):
            arr[i-r1][j-c1] = str((2*j)**2+1+(i-j))
        # (0, 0) 기준 오른쪽 삼각형 범위
        else:
            arr[i-r1][j-c1] = str((2*(j-1)+1)**2+(j-i))

        MAX = max(MAX, len(arr[i-r1][j-c1]))

for i in range(N):
    for j in range(M):
        print(" "*(MAX-len(arr[i][j])) + arr[i][j], end=' ')
    print()