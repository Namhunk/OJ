# 4 <= N <= 300
from heapq import heappush, heappop
def solution(land, height):
    N = len(land)
    heap = [(0, 0, 0)]
    visit = [[False]*N for _ in range(N)]
    
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = 0
    while heap:
        h, x, y = heappop(heap)
        if visit[x][y]: continue
        if h > height:
            answer += h
        
        visit[x][y] = True
        for r, c in move:
            nx, ny = x+r, y+c
            if not (0 <= nx < N and 0 <= ny < N): continue
            nh = abs(land[nx][ny] - land[x][y])
            heappush(heap, (nh, nx, ny))
            
    return answer
        

"""
모든 칸을 방문하기 위해 필요한 사다리 설치 비용의 최솟값

----------------------------------------------------
무작위 칸에서 모든 칸을 방문함
이동은 상, 하, 좌, 우

---------------------------------------------------------
heap으로 모든 위치를 저장
heap에 h_diff, x, y를 담음

h_diff가 작은 순서대로 방문
"""