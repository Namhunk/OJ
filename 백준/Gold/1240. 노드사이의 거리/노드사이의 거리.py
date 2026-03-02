import sys
input = sys.stdin.readline

from collections import deque
def solve():
    # 노드의 개수 N(2 <= N <= 1,000), 거리를 알고 싶은 노드 쌍의 개수 M(1 <= M <= 1,000)
    N, M = map(int, input().strip().split())
    nodes = [[] for _ in range(N+1)]      # 각 노드간의 관계를 저장할 배열

    for _ in range(N-1):
        # 연결된 두 점 a, b와 거리 d
        a, b, d = map(int, input().strip().split())
        nodes[a].append((b, d))
        nodes[b].append((a, d))


        
    for _ in range(M):
        a, b = map(int, input().strip().split())
        print(bfs(a, b, nodes, N))

def bfs(start, end, nodes, n):
    dist = [-1]*(n+1)
    q = deque([start])
    dist[start] = 0

    while q:
        x = q.popleft()
        if x == end:
            return dist[x]
        
        for nx, nd in nodes[x]:
            if dist[nx] >= 0: continue
            dist[nx] = dist[x] + nd
            q.append(nx)
    
    return -1

if __name__ == '__main__':
    solve()

"""
N개의 노트로 이루어진 트리가 주어지고 M개의 두 노드 쌍을 입력받을 때, 두 노드 사이의 거리를 출력

1
2 4
  3 5

트리의 루트를 1이라 가정할 때
하위 노드 들은
1까지의 거리가 누적됨

"""