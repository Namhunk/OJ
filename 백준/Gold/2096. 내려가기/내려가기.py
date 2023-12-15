import sys

# 첫 줄에서 시작해서 마지막 줄에서 끝나는 놀이
# 이동은 아래와 대각선
# 최대 점수와, 최소 점수는 구해라

# N 입력
N = int(sys.stdin.readline().strip())

# 최소, 최대 배열 생성 0번 행은 이전값, 1번 행은 이전 값과 현재 점수를 더한 값
MIN = [[0]*3 for _ in range(2)]
MAX = [[0]*3 for _ in range(2)]

# 입력을 하며 수행
for _ in range(N):
    # 현재 점수 리스트
    curr = list(map(int, sys.stdin.readline().strip().split()))
    
    # 1번 행에 이전 위치 중 현재 위치로 이동 가능한 값들만 현재 점수들과 더함
    MIN[1][0] = min(MIN[0][0] + curr[0], MIN[0][1] + curr[0])
    MAX[1][0] = max(MAX[0][0] + curr[0], MAX[0][1] + curr[0])
    
    MIN[1][1] = min(MIN[0][0] + curr[1], MIN[0][1] + curr[1], MIN[0][2] + curr[1])
    MAX[1][1] = max(MAX[0][0] + curr[1], MAX[0][1] + curr[1], MAX[0][2] + curr[1])
    
    MIN[1][2] = min(MIN[0][1] + curr[2], MIN[0][2] + curr[2])
    MAX[1][2] = max(MAX[0][1] + curr[2], MAX[0][2] + curr[2])
    
    # 이전 값들을 현재 값들로 최신화
    for j in range(3):
        MIN[0][j] = MIN[1][j]
        MAX[0][j] = MAX[1][j]

print(max(MAX[1]), min(MIN[1]))