import sys
input = sys.stdin.readline

# refer to https://blog.everdu.com/149

# 가능한 경로의 수를 1,000,000,007로 나눈 나머지를 출력

# 한 건물에서 인접한 다른 건물로 이동 하는 데 1분이 걸림
# D분만 산책을 할 예정

# D 입력 (1 <= D <= 1,000,000,000)
D = int(input().strip())

# 산책을 시작 한 지 D분 일 때, 정보 과학관에 도착해야 함
mod = int(1e9)+7

# 각 건물마다 번호를 매겨봄 정보 과학관 = 0, 전산관 = 1, 미래관 = 2, ..., 학생회관 = 7
matrix = ((0, 1, 1, 0, 0, 0, 0, 0), # 정보 과학관
         (1, 0, 1, 1, 0, 0, 0, 0), # 전산관
         (1, 1, 0, 1, 1, 0, 0, 0), # 미래관
         (0, 1, 1, 0, 1, 1, 0, 0), # 신양관
         (0, 0, 1, 1, 0, 1, 1, 0), # 한경직기념관
         (0, 0, 0, 1, 1, 0, 0, 1), # 진리관
         (0, 0, 0, 0, 1, 0, 0, 1), # 형남공학관
         (0, 0, 0, 0, 0, 1, 1, 0)) # 학생회관

"""
위의  maxtrix 가지고 행렬식을 만들면

R0(D) = [0, 1, 1, 0, 0, 0, 0, 0] [R0(D-1)]
R1(D) = [1, 0, 1, 1, 0, 0, 0, 0] [R1(D-1)]
R2(D) = [1, 1, 0, 1, 1, 0, 0, 0] [R2(D-1)]
R3(D) = [0, 1, 1, 0, 1, 1, 0, 0] [R3(D-1)]
R4(D) = [0, 0, 1, 1, 0, 1, 1, 0] [R4(D-1)]
R5(D) = [0, 0, 0, 1, 1, 0, 0, 1] [R5(D-1)]
R6(D) = [0, 0, 0, 0, 1, 0, 0, 1] [R6(D-1)]
R7(D) = [0, 0, 0, 0, 0, 1, 1, 0] [R7(D-1)]

R0(D) = R1(D-1) + R2(D-1) 처럼 식을 세울 수 있음
R1(D) = R0(D-1) + R2(D-1) + R3(D-1)
.
.
R7(D) = R5(D-1) + R6(D-1)
피보나치 행렬 곱과 비슷
"""

def mul(mat1, mat2):
    res = [[0]*len(mat2[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
                res[i][j] %= mod

        res[i] = tuple(res[i])

    res = tuple(res)
    return res

def solv(matrix, n):
    if n == 1:
        return matrix

    temp = solv(matrix, n//2)
    res = mul(temp, temp)

    if n % 2 == 1:
        res = mul(res, matrix)

    return res

ans = ((1,), (0,), (0,), (0,), (0,), (0,), (0,), (0,))

ans = mul(solv(matrix, D), ans)
print(ans[0][0])