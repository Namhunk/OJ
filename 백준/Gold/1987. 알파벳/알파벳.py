import sys

# 최대 거리를 구해라 (단, 이미 지난 알파벳은 지나갈 수 없음)

# 문자를 숫자로 변환 A = 0, B = 1..
def change(word): return ord(word) - 65
    
# 최대 거리를 구하는 함수
def Max_Distance(x, y, cnt):
    new_cnt = 0
    for r, c in move:
        if not (0 <= x+r < R and 0 <= y+c < C): continue # 보드의 범위를 벗어나지 않고
        if not visit[change(arr[x+r][y+c])]: continue # 방문하지 않았다면
        # 방문 표시
        visit[change(arr[x+r][y+c])] = 0
        new_cnt = max(new_cnt, Max_Distance(x+r, y+c, cnt+1))
        # 방문 표시 해제
        visit[change(arr[x+r][y+c])] = 1
    
    return max(cnt, new_cnt) 
# 세로 = R, 가로 = C
R, C = map(int, sys.stdin.readline().strip().split())

# 배열 입력
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]

# 이동 배열 (상, 하, 좌, 우)
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 방문 표시
visit = [1 for _ in range(26)]

# 시작 위치 방문 표시
visit[change(arr[0][0])] = 0

print(Max_Distance(0, 0, 1))