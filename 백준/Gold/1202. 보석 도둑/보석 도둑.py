import sys
from heapq import heappush, heappop

N, K = map(int, sys.stdin.readline().strip().split()) # N: 보석의 개수, K: 가방의 개수
MV = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)] # (무게, 가격)
C = sorted([int(sys.stdin.readline().strip()) for _ in range(K)]) # 각 가방에 담을 수 있는 최대 무게

MV.sort(key=lambda x: (x[0], -x[1])) # 무게 내림차순, 가치 오름차순으로 정렬

# 가방에는 최대 한 개의 보석만 넣을수 있다.
# 가격의 합의 최댓값 출력

ans = 0
heap = [] 
for i in range(K):
    while MV and C[i] >= MV[0][0]: # 보석이 남아있고, 현재 가방이 보석 무게보다 큰 경우
        heappush(heap, -MV[0][1]) # heap에 현재 가치 추가
        heappop(MV) # 보석 목록에서 제거
    
    if heap: ans += heappop(heap) # 가장 가치가 높은 보석 +
    if not heap and not MV: break
print(-ans)