import sys
input = sys.stdin.readline

# 최단 거리를 출력

# N (1 <= N <= 100,000)
N = int(input().strip())

# 레스토랑의 위치
P = list(map(int, input().strip().split()))

# N명의 X, Y 위치 (1 <= X, Y <= 100,000)
arr = [P]+[list(map(int, input().strip().split())) for _ in range(N)]

dp = [[float('inf')]*5 for _ in range(N+1)] # 각 거리 중앙, 상, 하, 좌, 우
dp[0] = [0]*5

position = [[[0, 0]]*5 for _ in range(N+1)] # 각 위치 중앙, 상, 하, 좌, 우
position[0] = [arr[0]]*5

def path(curr): # 주변의 위치를 반환
    x, y = curr
    ret = []
    move = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    for r, c in move:
        ret.append([x+r, y+c])

    return ret

def dist(curr, next): # 두 위치의 거리
    x1, y1 = curr
    x2, y2 = next
    return abs(x1-x2) + abs(y1-y2)

for i in range(1, N+1):
    P = path(arr[i])
    for j in range(5):
        position[i][j] = P[j]

    for j in range(5):
        for k in range(5):
            dp[i][j] = min(dp[i][j], dp[i-1][k] + dist(position[i-1][k], position[i][j]))


print(min(dp[-1]))


"""
케익을 배달하기 위해서는 고객의 위치나, 상하좌우 인접한 위치까지 가야함

예제 1을 예로 들면
고객의 위치가 (3, 6) 일 때, (2, 6), (3, 7), (4, 6), (3, 5) 총 5개의 위치에 놓아도 됨
dp[i][j], i : 고객의 위치, j : 고객의 상하좌우

"""