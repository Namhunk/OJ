# 3 <= len(matrix_sizes) <= 200
# 1 <= matrix_sizes[i] <= 200
def solution(matrix_sizes):
    N = len(matrix_sizes)
    dp = [[0 if i == j else float('inf') for j in range(N)] for i in range(N)]
    
    for length in range(2, N+1):
        for i in range(0, N-length+1):
            j = i + length - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost


    answer = dp[0][N-1]
    return answer
    
    
"""
a x b 인 행렬, b x c 인 행렬이 있음
두 행렬을 곱하려면 a x b x c 번 해야함

각 행렬의 크기 matrix_size가 주어질 때
모든 행렬을 곱하기 위한 최소 곱셈 연산 횟수 return

------------------------------------------
N개의 행렬이 주어질 때 
어떤 순서로 행렬곱을 수행할 것인지 

1. matrix_sizes가 행렬곱을 수행할 수 있는 순서로 주어지는가?
    - 위 문장이 가능하다는 가정하에 연산 순서만을 고려한 방법을 수행
"""