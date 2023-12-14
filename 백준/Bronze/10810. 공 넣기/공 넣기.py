import sys

N, M  = map(int, sys.stdin.readline().strip().split())

arr = [[0] for _ in range(N+1)]
# i번 부터 j번 바구니까지 k번 공을 넣는다.
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    for row in range(i, j+1):
        arr[row][0] = k

for i in arr[1:]:
    print(*i, end=" ")