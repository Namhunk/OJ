import sys

# N x N 행렬 A가 주어졌을 때, A의 B제곱을 구해라(단, A^B의 각 원소를 1000으로 나눠야 함)

def matmul(mat1, mat2):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000
    
    return result

# N, B 입력
N, B = map(int, sys.stdin.readline().strip().split())
mat = []
for _ in range(N):
    mat.append(list(map(int, sys.stdin.readline().strip().split())))

ans = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    ans[i][i] = 1

while True:
    if not B: break
    
    if B % 2: ans = matmul(mat, ans)
    mat = matmul(mat, mat)
    B //= 2

for i in ans:
    print(*i)