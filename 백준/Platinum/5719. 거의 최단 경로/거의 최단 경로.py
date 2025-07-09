import sys
input = sys.stdin.readline

# 거의 최단 경로란 최단 경로에 포함되지 않는 도로로만 이루어진 경로 중 가장 짧은 것
# 거의 최단 경로의 길이를 출력, 만약, 거의 최단 경로가 없는 경우 -1을 출력

from heapq import heappush, heappop
def dijkstra(start):
    dist = [float('inf')]*N
    dist[start] = 0
    heap = [[0, start]]

    while heap:
        d, x = heappop(heap)
        if d > dist[x]: continue
        for nd, nx in (edges[x]):
            if road[x][nx] == False: continue
            sd = d + nd
            if sd >= dist[nx]: continue
            dist[nx] = sd
            heappush(heap, [sd, nx])

    return dist

def except_road(dist, start, end):
    heap = [[dist[end], end]] # 역방향
    while heap:
        d, x = heappop(heap)
        if x == start: continue

        for bd, bx in back[x]:
            if road[bx][x] == False: continue
            if dist[bx] == dist[x]-bd:
                road[bx][x] = False
                heappush(heap, [dist[bx], bx])


while 1:
    # 장소의 수 N (2 <= N <= 500), 도로의 수 M (1 <= M <= 10**4)
    N, M = map(int, input().strip().split())

    if (N, M) == (0, 0): break # N, M 이 0 이면 종료

    # 시작점 S, 도착점 D (S != D; 0 <= S, D < N)
    S, D = map(int, input().strip().split())

    # 도로의 정보 U,V,P (U != V; 0 <= U, V < N; 1 <= P <+ 10**3)
    # U에서 V로 가는 도로의 길이가 P, U -> V 는 유향
    # U에서 V로 가는 도로는 최대 1개
    edges = [[] for _ in range(N)]
    back = [[] for _ in range(N)]
    road = [[True]*N for _ in range(N)]

    for _ in range(M):
        U, V, P = map(int, input().strip().split())
        edges[U].append([P, V])
        back[V].append([P, U])

    arr = dijkstra(S)
    except_road(arr, S, D)
    ans = dijkstra(S)

    print(ans[D] if ans[D] != float('inf') else -1)


"""
"""