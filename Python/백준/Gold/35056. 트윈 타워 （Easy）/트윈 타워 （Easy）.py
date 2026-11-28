import sys
import random, math
input = sys.stdin.readline

def solve(N, A, B):
    DP = [[[-float('inf')]*3 for _ in range(N+1)] for _ in range(N)]
    DP[0][0][0] = 0     # 아무것도 세우지 않는 경우
    DP[0][1][1] = A[0]  # 첫 위치에 타워를 세웠을때

    for i in range(1, N):
        for j in range(N+1):
            # 현재 위치에 타워를 세우지 않는 경우
            DP[i][j][0] = max(DP[i-1][j][0], DP[i-1][j][1], DP[i-1][j][2])

            if j >= 1: # 현재 위치에 타워를 세울 수 있는 경우는 j가 0보다 큰 경우
                DP[i][j][1] = max(DP[i-1][j-1][0], DP[i-1][j-1][1], DP[i-1][j-1][2]) + A[i]

                # 다리를 만들 수 있는 경우는 이전 위치에 타워를 세운 경우
                DP[i][j][2] = DP[i-1][j-1][1] + A[i] + B[i-1]

    for j in range(1, N+1):
        print(max(DP[N-1][j]))

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

현재 고려중인 타워가 i 일때
j개의 타워를 세워야 하고
k의 case로 선택

j = 1
0 1 2 3
1 2 3 4
0 0 0 0

j = 2
0 1  13  14
1 3  5   8
0 13 14  

arr[i][j][0] = max(arr[i-1][j][0], arr[i-1][j][1], arr[i-1][j][2])
arr[i][j][1] = max(arr[i-1][j-1][0], arr[i-1][j-1][1], arr[i-1][j-1][2]) + A[i]
arr[i][j][2] = arr[i-1][j-1][1] + A[i] + B[i-1]
"""