import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr1 = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
arr2 = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(arr1[i][j] + arr2[i][j], end=" ")
    print()