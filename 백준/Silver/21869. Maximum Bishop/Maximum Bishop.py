import sys
input = sys.stdin.readline

"""
N이 주어졌을 때, 최대한 많은 비숍을 서로 공격할 수 없도록 배치

배치할 수 있는 비숍의 최대 개수 M을 첫 번째 줄에 출력
이후 M개의 줄에 걸쳐 비숍을 배치해야 하는 행의 번호와 열의 번호를 출력 (행, 열은 1부터 시작)

체스판은 N x N 크기
"""
def solve(N):
    if N == 1:
        print(1)
        print(1, 1)
        return
    
    print(2 * N - 2)
    for i in range(1, N+1):
        print(1, i)

    for i in range(2, N):
        print(N, i)

N = int(input().strip())
solve(N)