import sys, heapq

# 1. 출발 도시에서 도착 도시까지 가는데 드는 최소 비용 출력
# 2. 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력(출발, 도착 도시 포함)
# 3. 최소 비용을 갖는 경로를 방문하는 도시 순서를 순서대로 출력

def dijkstra(start, end): # 시작, 종료 위치를 가지고 다익스트라 수행
    dp = [float('inf')] * (n+1) # 비용 저장 배열
    dp[start] = 0 # 시작위치 비용 0 으로 설정
    
    heap = []
    heapq.heappush(heap, (0, start, [start])) # 현재 비용, 위치, 이동 경로 저장 
    
    while heap:
        cc, cn, cp = heapq.heappop(heap) # 현재 비용, 위치, 경로
        if cc <= dp[cn]: # 현재 비용이 최소 비용보다 작거나 같으면
            if cn == end: return dp[cn], cp # 현재 위치가 도착위치면 최소 비용, 경로 반환
            for nc, nn in arr[cn]: # 다음 비용, 위치
                SUM = cc + nc # 현재 비용과 다음 비용의 합
                if SUM < dp[nn]: # 비용의 합이 현재 위치의 최소 비용보다 작다면
                    dp[nn] = SUM
                    heapq.heappush(heap, (SUM, nn, [*cp, nn]))

# 도시의 개수 n 입력
n = int(sys.stdin.readline().strip())

# 버스의 개수 m 입력
m = int(sys.stdin.readline().strip())

# 각 도시의 버스 정보를 저장할 배열 생성 0 ~ n까지
arr = [[] for _ in range(n+1)]

# m+2줄까지 버스에 정보 입력 : 출발, 도착, 비용 순서
for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().strip().split()) # s -> e 로 c 의 비용
    arr[s].append((c, e)) # 시작 위치에서 비용, 도착 위치 저장

# 구하고자 하는 출발점의 도시 번호, 도착점의 도시번호
start, end = map(int, sys.stdin.readline().strip().split())

cost, path = dijkstra(start, end) # 최소 비용, 경로를 받음

print(cost)
print(len(path))
print(*path)