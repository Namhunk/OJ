import sys
import random, math
input = sys.stdin.readline

def solve(N, A, B):
    DP = [[0]*(N) for _ in range(N)]

    DP[0][0] = A[0]
    for i in range(1, N):
        DP[i][0] = max(DP[i-1][0], A[i])

    for i in range(1, N):
        for j in range(i+1):
            if j > 0:
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-1] + A[i], DP[i-2][j-2] + A[i] + A[i-1] + B[i-1])

    for i in DP[-1]:
        print(i)

def main():
    # 2 <= N <= 2000
    N = int(input().strip())
    # 0 <= A[i] <= 10**9
    A = list(map(int, input().strip().split()))
    # 0 <= B[i] <= 10**9
    B = list(map(int, input().strip().split()))

    solve(N, A, B)

if __name__ == '__main__':
    main()  

"""
일렬로 이어진 N개의 개발부지가 있음

1. i번 부지에 타워를 지으면 도시는 A[i]만큼의 가치를 얻고 1의 비용을 소모
2. i번 부지와 i+1번 부지에 둘 다 타워가 있다면, i번 타워와 i+1번사이에 통로를 만들고 B[i]가치를 얻음
3. 하나의 타워에는 하나의 통로만 연결가능

N개의 줄에 걸쳐서 비용 i로 얻을 수 있는 최대 가치

-----------------------------------------------------


1. 현재 위치에 타워를 세우지 않는 경우
2. 현재 위치에 타워를 세우는 경우
3. 이전 위치와 다리가 연결된 경우

2차원 배열로 수행할때, 0부터 i 까지 위치들 중 j개를 선택할 때
1   1   1   1  
2  13  13  13
3  14  15  15
4   8  18  21

DP[i][j] = max(DP[i-1][j], DP[i-1][j-1] + A[i], DP[i-2][j-2] + A[i] + A[i-1] + B[i])
"""