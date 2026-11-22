import sys
input = sys.stdin.readline

from heapq import heappush, heappop
def solve(N, M):
    road = [[] for _ in range(M)]

    total = 0
    for _ in range(N):
        x, y, z = map(int, input().strip().split())
        road[x].append((z, y))
        road[y].append((z, x))
        total += z
    
    visit = [-1]*M
    heap = [(0, 0)] # 0부터 시작
    while heap:
        c, x = heappop(heap)
        if visit[x] >= 0: continue

        visit[x] = c    
        for nc, nx in sorted(road[x]):
            if visit[nx] < 0:
                heappush(heap, (nc, nx))
        
    print(total - sum(visit))

if __name__ == '__main__':
    while 1:
        # 집의 수 M, 길의 수 N (1 <= M <= 200,000, M-1 <= N <= 200,000)
        M, N = map(int, input().strip().split())
        if M == 0 and N == 0: break
        solve(N, M)

"""
도시는 연결 그래프의 형태, 도시상 모든 길의 거리 합은 2^31보다 작음

도시에 있는 모든 두 집쌍에 대해, 불이 켜진 길만으로 서로를 왕래할 수 있는 최소 거리

모든 도시가 연결되어 있으면 됨

MST

"""