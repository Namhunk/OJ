import sys
input = sys.stdin.readline

from heapq import heappush, heappop
def solve():
    # 컴퓨터의 수 (1 <= N <= 1,000)
    N = int(input().strip())
    
    connection = [[] for _ in range(N+1)]
    # 연결할 수 있는 선의 수(1 <= M <= 100,000)
    M = int(input().strip())
    
    for _ in range(M):
        # a, b를 연결하는 비용 c (a == b 일 수도)
        a, b, c = map(int, input().strip().split())
        connection[a].append((c, b))
        connection[b].append((c, a))
    
    visit = [False]*(N+1)
    ans = 0

    heap = [(0, 1)]
    while heap:
        c, x = heappop(heap)
        if visit[x]: continue
        visit[x] = True
        ans += c
        for nc, nx in sorted(connection[x]):
            if visit[nx]: continue
            heappush(heap, (nc, nx))

    print(ans)

if __name__ == '__main__':
    solve()

"""
컴퓨터를 연결하는 비용을 최소로 해서 연결하는 방법
그래프에서 간선의 비용을 최소로 하는 사이클을 구하는 코드

"""