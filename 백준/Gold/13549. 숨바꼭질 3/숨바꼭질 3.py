import heapq, sys

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 출력

# 수빈이의 위치 = N, 동생의 위치 = K
N, K = map(int, sys.stdin.readline().strip().split())

visit = [True]*(int(1e5)+1) # 최대 범위를 갖는 방문 배열 생성
visit[N] = False # 수빈이의 위치 방문 처리
heap = [(0, N)] # 최소 시간을 구해야 하므로 (시간, 위치)

move = [-1, 1, N] # 이동거리 배열
while heap:
    T, X = heapq.heappop(heap) # T=시간, X=위치 (시간이 작은 순으로 뽑아냄)
    
    if X == K: print(T); break # 현재 위치가 동생과 같다면 시간 출력
    
    move[2] = X # 현재 위치의 2배로 설정
    for i in move:
        if not (0 <= X+i < len(visit)): continue # 다음 위치가 범위를 벗어나지 않는다면
        if not visit[X+i]: continue # 방문하지 않은 위치라면
        
        visit[X+i] = False
        if X == i: heapq.heappush(heap, (T, X+i)) # 2배 거리는 현재 시간
        else: heapq.heappush(heap, (T+1, X+i)) # 나머지는 현재 시간 + 1