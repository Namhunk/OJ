# 3 <= n <= 8
# 3 <= m <= 8
# 1 <= len(d) <= 100
# 1 <= k <= 10**9
def solution(grid, d, k):
    answer = 0
    
    MOD = 10**9+7
    
    n = len(grid)
    m = len(grid[0])
    l = n * m
    
    route = get_route(grid, d) # 경로 배열 구하기
    
    result = [[0]*l for _ in range(l)]
    for i in range(l): # 단위 행렬로
        result[i][i] = 1
    
    while k:
        if k & 1:
            result = mat_mul(route, result, MOD)
        
        route = mat_mul(route, route, MOD)
        k >>= 1
    
    for i in range(l):
        answer = (answer + sum(result[i])) % MOD
    
    return answer

def mat_mul(A, B, MOD):
    l = len(A)
    C = [[0]*l for _ in range(l)]
    
    for i in range(l):
        for k in range(l):
            if A[i][k] == 0: continue # 결국 A, B는 같은 값을 가진 배열 0이면 건너뜀
            for j in range(l):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    
    return C

from collections import defaultdict
def get_route(grid, d):
    MOD = 10**9+7 # 개수의 최대값
    
    n = len(grid)
    m = len(grid[0])
    
    l = n * m # 새로운 배열의 크기
    route = [[0]*l for _ in range(l)]
    
    move = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상하좌우 이동
    
    for start in range(l): # 모든 n x m 위치
        cur = {start: 1} # 현재 위치, 경로 개수
        
        for t in range(len(d)): # 총 len(d)번 이동
            nxt = defaultdict(int)
            for pos, cnt in cur.items():
                x, y = pos // m, pos % m
                for dx, dy in move:
                    nx, ny = x+dx, y+dy
                    if not (0 <= nx < n and 0 <= ny < m): continue # 범위를 벗어나지 않고
                    if grid[nx][ny] - grid[x][y] != d[t]: continue # 값을 만족한다면
                    
                    nxt[nx*m+ny] = (nxt[nx*m+ny] + cnt) % MOD
            
            cur = nxt
        
        for end, cnt in cur.items(): # len(d)번 이동이 끝난 후
            route[start][end] = cnt
    
    return route
                    

'''
* 격자 내에서 조건을 만족하는 경로의 수를 10^9+7 로 나눈 나머지 return

- 경사로 테스트는 n x m 크기의 격자 공간에서 진행
- 각 칸의 숫자는 높이
- 이동은 상하좌우
- 전기차가 인접한 칸으로 이동하는 길의 경사는 (이동하려는 칸의 높이) - (현재 칸의 높이)
- 경사 수열 d(전기차가 이동할 길의 경사), d[i] = 전기차가 i+1 번째로 이동할 때 경사가 d[i]인 길을 지나야 함을 나타냄
- 전기차가 경사로를 반복적으로 이동할 때 받는 스트레스를 관찰하기 위해 주어진 경사수열을 k번 반복할 수 있는 경로를 찾아야함
(같은 칸 여러번 방문 가능, 지나온 길 되돌아가기 가능)

----------------------------------------------------------------
결국 전체의 경로 개수를 반환해야 함
새로운 배열 route를 생성 route[s][e] = s에서 출발해 e까지 가는 경로의 개수
모든 위치에 대한 개수니까 len(route) = n x m
'''