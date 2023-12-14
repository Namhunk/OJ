import sys
from collections import deque


def BFS(start, finish=0):
    global n

    que = deque()
    que.append((start, 0))

    visited = [0] * (n+1)

    res = 0
    maxNode = 0

    while que:
        node, dist = que.popleft()
        visited[node] = 1

        # 출발지가 정해져 있다면 거리의 합을 리턴
        if finish and node == finish:
            return dist

        for next_node in tree[node]:
            # 방문하지 않은 노드 탐색
            if visited[next_node[0]]:
                continue

            if res < dist+next_node[1]:
                res = dist + next_node[1]
                maxNode = next_node[0]
            que.append((next_node[0], dist+next_node[1]))

    return maxNode

# 노드 개수
n = int(sys.stdin.readline().strip())
tree = [[] for _ in range(n+1)]
# 간선 입력
for _ in range(n-1):
    p, c, e = map(int, sys.stdin.readline().strip().split())
    tree[p].append((c, e))
    tree[c].append((p, e))

# 가장 멀리 떨어진 노드를 구함
v = BFS(1)
# 노드 v와 가장 멀리 떨어진 노드를 구함
e = BFS(v)

print(BFS(v, e))