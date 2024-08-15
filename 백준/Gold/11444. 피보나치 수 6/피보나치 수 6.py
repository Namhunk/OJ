import sys

# 행렬곱 연산
def mat_mul(mat1, mat2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= (int(1e9)+7)
    
    return result

# n 입력
n = int(sys.stdin.readline().strip())
ans = [[1, 0], [0, 1]]
fib_mat = [[1, 1], [1, 0]]

while n > 0:
    if n % 2 == 1:
        ans = mat_mul(ans, fib_mat)
    fib_mat = mat_mul(fib_mat, fib_mat)

    n//= 2

print(ans[1][0])
"""
원리

F(N) = F(N-1) + F(N-2)를 행렬곱 형태로 만든다면

F(N) = [F(N-1) F(N-2)][1]
                      [1]

                      
[F(N+1)]   [1 1] [F(N)  ]
[F(N)  ] = [1 0] [F(N-1)]

[F(N)  ]   [1 1] [F(N-1)]
[F(N-1)] = [1 0] [F(N-2)]

대입하면

[F(N+1)]   [1 1]^2 [F(N-1)]
[F(N)  ] = [1 0]   [F(n_2)]

[F(N+1) F(N)]   [1 1]^(n-1) [F2 = 1 F1 = 1]
[F(N) F(N-1)] = [1 0]       [F1 = 1 F0 = 0]

[F(N+1) F(N)]   [1 1]^n
[F(N) F(N-1)] = [1 0]


"""