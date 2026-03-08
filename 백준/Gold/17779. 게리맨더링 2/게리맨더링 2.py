import sys
input = sys.stdin.readline

def solve():
    global N, arr, dp
    # 맵의 크기 N (5 <= N <= 20)
    N = int(input().strip())

    arr = [[0]*(N+1)] # 구역의 인구를 저장할 배열
    for _ in range(N):
        arr.append([0]+list(map(int, input().strip().split())))
    
    dp = [[0]*(N+1) for _ in range(N+1)] # 누적 인원을 저장할 배열
    # 각 구역의 인구수를 먼저 더함 -> arr[r][c]는 x:(1->r), y:(1->y) 범위의 모든 값을 더한게 됨
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]
    
    # 조건을 만족하는 모든 x, y, d1, d2값을 구함
    temp = []
    for x in range(1, N+1):
        for y in range(1, N+1):
            for d1 in range(1, N+1):
                for d2 in range(1, N+1):
                    if not (1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N): continue
                    temp.append((x, y, d1, d2))
    
    ans = float('inf') # 정답을 저장할 변수
    for x, y, d1, d2 in temp:
        area, area_5 = set_area(x, y, d1, d2)
        r1, c1, r2, c2, r3, c3, r4, c4 = find_point(x, y, d1, d2)
        area_cnt = []
        # 구역 1의 인원 수
        cnt = dp[r1][c1] - area_5_cnt(1, 1, r1, c1, area)
        area_cnt.append(cnt)

        # 구역 2의 인원 수
        cnt = dp[r2][c2] - dp[r2][c1] - area_5_cnt(1, c1+1, r2, c2, area)
        area_cnt.append(cnt)

        # 구역 3의 인원 수
        cnt = dp[r3][c3] - dp[r1][c3] - area_5_cnt(r1+1, 1, r3, c3, area)
        area_cnt.append(cnt)

        # 구역 4의 인원 수
        cnt = dp[r4][c4] - dp[r2][c4] - dp[r4][c3] + dp[r2][c3] - area_5_cnt(r2+1, c3+1, r4, c4, area)
        area_cnt.append(cnt)

        # 구역 5의 인원 수
        area_cnt.append(area_5)

        cal = max(area_cnt) - min(area_cnt)
        ans = min(ans, cal)

    return ans

def area_5_cnt(sx, sy, ex, ey, area): # 해당 범위에서 선거구 5에 포함된 값을 반환
    ret = 0
    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            if area[i][j] == 5:
                ret += arr[i][j]
    
    return ret
            
# 각 선거구의 경계와 가장 가까운 번호들을 구함(1-4 선거구만 반환)
def find_point(x, y, d1, d2):
    # 1 번 선거구의 r1, c1 위치
    r1, c1 = x+d1-1, y

    # 2번 선거구의 r2, c2 위치
    r2, c2 = x+d2, N

    # 3번 선거구의 r3, c3 위치
    r3, c3 = N, y-d1+d2-1
    
    # 4번 선거구의 r4, c4 위치
    r4, c4 = N, N

    return r1, c1, r2, c2, r3, c3, r4, c4

# 현재 x, y, d1, d2 값 일때 5번 선거구들의 위치를 표시할 배열 반환
def set_area(x, y, d1, d2): 
    lines = {}
    # 1, 4 경계선
    for i in range(d1+1):
        nx, ny = x+i, y-i
        if 1 <= nx <= N and 1 <= ny <= N:
            lines[nx] = lines.get(nx, set())
            lines[nx].add(ny)
        
        nx, ny = x+d2+i, y+d2-i
        if 1 <= nx <= N and 1 <= ny <= N:
            lines[nx] = lines.get(nx, set())
            lines[nx].add(ny)
    
    # 2, 3 경계선
    for i in range(d2+1):
        nx, ny = x+i, y+i
        if 1 <= nx <= N and 1 <= ny <= N:
            lines[nx] = lines.get(nx, set())
            lines[nx].add(ny)
        
        nx, ny = x+d1+i, y-d1+i
        if 1 <= nx <= N and 1 <= ny <= N:
            lines[nx] = lines.get(nx, set())
            lines[nx].add(ny)
    
    area = [[0]*(N+1) for _ in range(N+1)] # 반환할 배열
    area_5 = 0
    # 범위 안의 모든 위치를 5로 표시
    for k, vals in lines.items():
        vals = sorted(vals)
        for v in range(vals[0], vals[-1]+1):
            area[k][v] = 5
            area_5 += arr[k][v]
    
    return area, area_5


if __name__ == '__main__':
    print(solve())

"""
맵의 크기는 N x N

인구가 가장 많은 선거구와 가장 적은 선거구 인구 차이의 최솟값 출력

구역을 5개로 나눠야 함
구역을 나누는 방법
1. 기준점 (x, y)와 경계의 길이 d1, d2를 정함 (d1, d2 >= 1, 1 <= x <= x+d1+d2 <= N, 1<= y-d1 < y < y+d2 <=N)
2.  1번 경계선: (x+d1, y-d1)
    2번 경계선: (x+d2, y+d2)
    3번 경계선: (x+d1+d2, y-d1+d2)
    4번 경계선: (x+d2+d1, y+d2-d1)

- 구역을 5개로 나누고, 각 구역의 인원수를 합해 구역별 최대, 최소 인원수의 차이를 구해야 함

1. 모든 구역들의 값을 더함
2. 기준점을 구하고 경계선을 그어줌
3.  선거구 1: arr[r1][c1] - (포함된 5 선거구 인원수)
    선거구 2: arr[r2][N]  - arr[r2][c1] - (포함된 5 선거구 인원수)
    선거구 3: arr[N][c3]  - arr[r1][c3] - (포함된 5 선거구 인원수)
    선거구 4: arr[N][N]   - arr[r2][N] - arr[N][c3] + arr[r2][c3] - (포함된 5 선거구 인원수)

    

"""