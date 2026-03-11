import sys
input = sys.stdin.readline

from collections import deque
def solve():
    global N, size, visit
    # N(0 <= N <= 100,000), K(0 <= K <= 100,000)
    N, K = map(int, input().strip().split())

    size = 100_001 # 최대 크기
    parent = [-1]*size
    visit = [-1]*size
    visit[N] = 0
    q = deque([N])
    while q:
        X = q.popleft()

        if X == K: break

        if 0 <= X-1 < size and visit[X-1] < 0:
            parent[X-1] = X
            visit[X-1] = visit[X]+1
            q.append(X-1)
        
        if 0 <= X+1 < size and visit[X+1] < 0:
            parent[X+1] = X
            visit[X+1] = visit[X]+1
            q.append(X+1)
        
        if 0 <= X*2 < size and visit[X*2] < 0:
            parent[X*2] = X
            visit[X*2] = visit[X]+1
            q.append(X*2)
    
    X = K
    route = [K]
    for _ in range(visit[K]):
        X = parent[X]
        route.append(X)
    
    print(visit[K])
    print(*route[::-1])
        
if __name__ == '__main__':
    solve()

"""
A가 점 N에서 시작, B가 점 K에 있을 때
A는 걷거나 순간이동을 할 수 있음
A의 위치가 X일 때 걷는다면 1초 뒤 X-1 or X+1로 이동 순간이동은 1초 뒤 2*X로 이동

가장 빠르게 찾을 수 있는 시간이 몇 초인지 구해라

"""